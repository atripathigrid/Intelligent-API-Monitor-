import pytest
from fastapi import Request
from fastapi.testclient import TestClient
from app.main import app
from app.decorators import circuit_breaker


client = TestClient(app)



# test API key 
def test_api_key_missing():
    response = client.get("/api/fetch-live")
    assert response.status_code == 401


def test_api_key_valid():
    response = client.get(
        "/api/fetch-live",
        headers={"x-api-key": "test_api_key"}  # must match your .env API_KEY
    )
    assert response.status_code == 200



#test circuit breaker

# Fake function to simulate failure
@circuit_breaker
async def failing_function():
    raise Exception("API failure")


@pytest.mark.asyncio
async def test_circuit_breaker():
    # Call multiple times to trigger breaker
    result1 = await failing_function()
    result2 = await failing_function()
    result3 = await failing_function()
    result4 = await failing_function()  # should be blocked

    assert result1 == {}
    assert result2 == {}
    assert result3 == {}
    assert result4 == {}  # circuit breaker active