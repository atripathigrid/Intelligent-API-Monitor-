import pytest
from app.services.weather import fetch_weather
from app.services.finance import fetch_finance
from app.services.geology import fetch_earthquake


@pytest.mark.asyncio
async def test_fetch_weather():
    data = await fetch_weather()
    assert isinstance(data, dict)


@pytest.mark.asyncio
async def test_fetch_finance():
    data = await fetch_finance()
    assert isinstance(data, dict)


@pytest.mark.asyncio
async def test_fetch_earthquake():
    data = await fetch_earthquake()
    assert isinstance(data, dict)