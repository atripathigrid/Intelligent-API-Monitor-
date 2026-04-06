from app.models import WeatherData, FinanceData, EarthquakeData


def stream_data(db):
    weather = db.query(WeatherData).all()
    finance = db.query(FinanceData).all()
    earthquake = db.query(EarthquakeData).all()

    yield "=== WEATHER DATA ===\n"
    for w in weather:
        yield f"{w.temperature}, {w.windspeed}, {w.timestamp}\n"

    yield "\n=== FINANCE DATA ===\n"
    for f in finance:
        yield f"{f.base_currency}, {f.usd_rate}, {f.eur_rate}, {f.timestamp}\n"

    yield "\n=== EARTHQUAKE DATA ===\n"
    for e in earthquake:
        yield f"{e.magnitude}, {e.place}, {e.timestamp}\n"