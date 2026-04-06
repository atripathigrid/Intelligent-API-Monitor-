from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_health():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"status": "running"}


def test_weather_endpoint():
    response = client.get("/api/weather")
    assert response.status_code == 200


def test_finance_endpoint():
    response = client.get("/api/finance")
    assert response.status_code == 200


def test_earthquake_endpoint():
    response = client.get("/api/earthquake")
    assert response.status_code == 200


def test_anomalies_endpoint():
    response = client.get("/api/anomalies")
    assert response.status_code == 200