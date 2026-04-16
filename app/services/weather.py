import httpx
from app.decorators import circuit_breaker
from app.utils.logger import logger


@circuit_breaker
async def fetch_weather():
    url = "https://api.open-meteo.com/v1/forecast?latitude=28.61&longitude=77.23&current_weather=true"

    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(url, timeout=10)

            # Check response status
            if response.status_code != 200:
                logger.error(f"Weather API failed with status {response.status_code}")
                return {}

            data = response.json()

            logger.info("Weather API data fetched successfully")
            return data

    except Exception as e:
        logger.error(f"Error fetching weather data: {e}")
        return {}