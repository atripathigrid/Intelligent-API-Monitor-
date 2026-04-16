from app.config import settings
from app.utils.logger import logger


def detect_anomalies(weather, finance, earthquake):
    anomalies = []

    # Temperature anomaly
    if weather.temperature > settings.MAX_TEMP_THRESHOLD:
        message = (
            f"High temperature: {weather.temperature} "
            f"(threshold: {settings.MAX_TEMP_THRESHOLD})"
        )
        logger.warning(message)
        anomalies.append(message)

    # Finance anomaly
    if finance.usd_rate < settings.MIN_USD_EUR_THRESHOLD:
        message = (
            f"Low USD rate: {finance.usd_rate} "
            f"(threshold: {settings.MIN_USD_EUR_THRESHOLD})"
        )
        logger.warning(message)
        anomalies.append(message)

    # Earthquake anomaly
    if earthquake.magnitude > settings.MAX_EARTHQUAKE_MAGNITUDE:
        message = (
            f"High earthquake magnitude: {earthquake.magnitude} "
            f"(threshold: {settings.MAX_EARTHQUAKE_MAGNITUDE})"
        )
        logger.warning(message)
        anomalies.append(message)

    return anomalies