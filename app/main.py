from fastapi import FastAPI, Depends, BackgroundTasks
from fastapi.responses import StreamingResponse
import asyncio

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
from app.crud import create_weather, create_finance, create_earthquake

# Utils
from app.utils.anomaly import detect_anomalies
from app.utils.export import stream_data

app = FastAPI()

# Create tables
Base.metadata.create_all(bind=engine)


# DB Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Health Route
@app.get("/")
def health():
    return {"status": "running"}


# Fetch and Store Data
@app.get("/api/fetch-live")
async def fetch_live(background_tasks: BackgroundTasks, db=Depends(get_db)):
    weather_data, finance_data, earthquake_data = await asyncio.gather(
        fetch_weather(),
        fetch_finance(),
        fetch_earthquake()
    )

    weather = weather_data.get("current_weather", {})
    weather_clean = WeatherSchema(
        temperature=weather.get("temperature", 0),
        windspeed=weather.get("windspeed", 0)
    )

    finance_clean = FinanceSchema(
        base=finance_data.get("base", "EUR"),
        usd_rate=finance_data.get("rates", {}).get("USD", 0),
        eur_rate=finance_data.get("rates", {}).get("EUR", 0)
    )

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

    create_weather(db, weather_clean)
    create_finance(db, finance_clean)
    create_earthquake(db, earthquake_clean)

    background_tasks.add_task(
        detect_anomalies,
        weather_clean,
        finance_clean,
        earthquake_clean
    )

    return {"message": "Data fetched & stored successfully"}


# Weather Data
@app.get("/api/weather")
def get_weather(db=Depends(get_db)):
    return db.query(models.WeatherData).all()


# Finance Data
@app.get("/api/finance")
def get_finance(db=Depends(get_db)):
    return db.query(models.FinanceData).all()


# Earthquake Data
@app.get("/api/earthquake")
def get_earthquake(db=Depends(get_db)):
    return db.query(models.EarthquakeData).all()


# Anomalies Route
@app.get("/api/anomalies")
def get_anomalies():
    return {
        "anomalies": [
            "High temperature detected",
            "USD rate below threshold",
            "Earthquake magnitude too high"
        ]
    }


# Export Route
@app.get("/api/export")
def export_data(db=Depends(get_db)):
    return StreamingResponse(
        stream_data(db),
        media_type="text/plain"
    )