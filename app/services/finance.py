import httpx
from app.decorators import circuit_breaker
from app.utils.logger import logger


@circuit_breaker
async def fetch_finance():
    url = "https://api.exchangerate-api.com/v4/latest/EUR"

    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(url, timeout=10)

            # Check if API failed
            if response.status_code != 200:
                logger.error(f"Finance API failed with status {response.status_code}")
                return {}

            data = response.json()

            logger.info("Finance API data fetched successfully")
            return data

    except Exception as e:
        logger.error(f"Error fetching finance data: {e}")
        return {}