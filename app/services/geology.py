import httpx


async def fetch_earthquake():
    url = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_day.geojson"

    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        return response.json()