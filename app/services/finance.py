import httpx


async def fetch_finance():
    url = "https://api.exchangerate-api.com/v4/latest/EUR"

    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        return response.json()