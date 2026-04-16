import httpx
from app.decorators import circuit_breaker
from app.utils.logger import logger


@circuit_breaker
async def fetch_earthquake():
    url = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_day.geojson"

    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(url, timeout=10)

            # Check response status
            if response.status_code != 200:
                logger.error(f"Earthquake API failed with status {response.status_code}")
                return {}

            data = response.json()

            logger.info("Earthquake API data fetched successfully")
            return data

    except Exception as e:
        logger.error(f"Error fetching earthquake data: {e}")
        return {}