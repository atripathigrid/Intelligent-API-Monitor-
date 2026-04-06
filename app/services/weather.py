import httpx


async def fetch_weather():
    url = "https://api.open-meteo.com/v1/forecast?latitude=28.61&longitude=77.23&current_weather=true"

    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        return response.json()