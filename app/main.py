from fastapi import FastAPI, Depends, BackgroundTasks, Request
from fastapi.responses import StreamingResponse
import asyncio

# Logger
from app.utils.logger import logger

# DB
from app.database import SessionLocal, Base, engine
import app.models as models  

# Services
from app.services.weather import fetch_weather
from app.services.finance import fetch_finance
from app.services.geology import fetch_earthquake

# Schemas
from app.schemas import WeatherSchema, FinanceSchema, EarthquakeSchema

# CRUD
from app.crud import create_weather, create_finance, create_earthquake, create_alert

# Utils
from app.utils.anomaly import detect_anomalies
from app.utils.export import stream_data

# Decorator
from app.decorators import require_api_key

app = FastAPI()

# Create tables
Base.metadata.create_all(bind=engine)
logger.info("Database tables created successfully")


# DB Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Background task for anomaly processing
def process_anomalies(weather, finance, earthquake):
    db = SessionLocal()

    try:
        anomalies = detect_anomalies(weather, finance, earthquake)

        for anomaly in anomalies:
            logger.warning(f"Anomaly detected: {anomaly}")
            create_alert(db, "threshold", anomaly)

    finally:
        db.close()


# Health Route
@app.get("/")
def health():
    logger.info("Health endpoint called")
    return {"status": "running"}


# =========================================================
# 🔐 SECURED ENDPOINT (FIXED DECORATOR IMPLEMENTATION)
# =========================================================
@app.get("/api/fetch-live")
@require_api_key
async def fetch_live(
    request: Request,
    background_tasks: BackgroundTasks,
    db=Depends(get_db)
):
    logger.info("Fetching live data from external APIs")

    try:
        weather_data, finance_data, earthquake_data = await asyncio.gather(
            fetch_weather(),
            fetch_finance(),
            fetch_earthquake()
        )
    except Exception as e:
        logger.error(f"Error fetching external APIs: {e}")
        return {"error": "Failed to fetch external data"}

    # Weather processing
    weather = weather_data.get("current_weather", {})
    weather_clean = WeatherSchema(
        temperature=weather.get("temperature", 0),
        windspeed=weather.get("windspeed", 0)
    )

    # Finance processing
    finance_clean = FinanceSchema(
        base=finance_data.get("base", "EUR"),
        usd_rate=finance_data.get("rates", {}).get("USD", 0),
        eur_rate=finance_data.get("rates", {}).get("EUR", 0)
    )

    # Earthquake processing
    features = earthquake_data.get("features", [])

    if features:
        quake = features[0]["properties"]
        earthquake_clean = EarthquakeSchema(
            magnitude=quake.get("mag", 0),
            place=quake.get("place", "unknown")
        )
    else:
        earthquake_clean = EarthquakeSchema(
            magnitude=0,
            place="no data"
        )

    # DB Storage
    create_weather(db, weather_clean)
    create_finance(db, finance_clean)
    create_earthquake(db, earthquake_clean)

    logger.info("Data stored successfully in database")

    # Background task
    background_tasks.add_task(
        process_anomalies,
        weather_clean,
        finance_clean,
        earthquake_clean
    )

    logger.info("Anomaly detection task triggered")

    return {"message": "Data fetched & stored successfully"}


# Weather Data
@app.get("/api/weather")
def get_weather(db=Depends(get_db)):
    logger.info("Fetching weather data from DB")
    return db.query(models.WeatherData).all()


# Finance Data
@app.get("/api/finance")
def get_finance(db=Depends(get_db)):
    logger.info("Fetching finance data from DB")
    return db.query(models.FinanceData).all()


# Earthquake Data
@app.get("/api/earthquake")
def get_earthquake(db=Depends(get_db)):
    logger.info("Fetching earthquake data from DB")
    return db.query(models.EarthquakeData).all()


# Anomaly Route
@app.get("/api/anomalies")
def get_anomalies(db=Depends(get_db)):
    logger.info("Fetching anomalies from database")

    anomalies = db.query(models.AnomalyAlert).all()

    return {
        "anomalies": [
            {
                "type": a.alert_type,
                "message": a.message,
                "timestamp": a.timestamp
            }
            for a in anomalies
        ]
    }


# Export Route
@app.get("/api/export")
def export_data(db=Depends(get_db)):
    logger.info("Export endpoint called")
    return StreamingResponse(
        stream_data(db),
        media_type="text/plain"
    )