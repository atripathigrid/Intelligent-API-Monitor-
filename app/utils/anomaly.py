from app.config import settings


def detect_anomalies(weather, finance, earthquake):
    anomalies = []

    if weather.temperature > settings.MAX_TEMP_THRESHOLD:
        anomalies.append(
            f"High temperature detected: {weather.temperature}"
        )

    if finance.usd_rate < settings.MIN_USD_EUR_THRESHOLD:
        anomalies.append(
            f"USD rate below threshold: {finance.usd_rate}"
        )

    if earthquake.magnitude > settings.MAX_EARTHQUAKE_MAGNITUDE:
        anomalies.append(
            f"High earthquake magnitude detected: {earthquake.magnitude}"
        )

    return anomalies