from app.models import WeatherData, FinanceData, EarthquakeData, AnomalyAlert


def create_weather(db, weather):
    weather_obj = WeatherData(
        temperature=weather.temperature,
        windspeed=weather.windspeed
    )

    db.add(weather_obj)
    db.commit()
    db.refresh(weather_obj)

    return weather_obj


def create_finance(db, finance):
    finance_obj = FinanceData(
        base_currency=finance.base,
        usd_rate=finance.usd_rate,
        eur_rate=finance.eur_rate
    )

    db.add(finance_obj)
    db.commit()
    db.refresh(finance_obj)

    return finance_obj


def create_earthquake(db, earthquake):
    earthquake_obj = EarthquakeData(
        magnitude=earthquake.magnitude,
        place=earthquake.place
    )

    db.add(earthquake_obj)
    db.commit()
    db.refresh(earthquake_obj)

    return earthquake_obj


def create_alert(db, alert_type, message):
    alert = AnomalyAlert(
        alert_type=alert_type,
        message=message
    )

    db.add(alert)
    db.commit()
    db.refresh(alert)

    return alert