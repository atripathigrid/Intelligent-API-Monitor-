#import testclient
from fastapi.testclient import TestClient
from app.main import app
#create client
client = TestClient(app)

#test:health endpoint
def test_health():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"status": "running"}

#test:weather
def test_weather_endpoint():
    response = client.get("/api/weather")
    assert response.status_code == 200

#test:finance
def test_finance_endpoint():
    response = client.get("/api/finance")
    assert response.status_code == 200

#test:earthquake
def test_earthquake_endpoint():
    response = client.get("/api/earthquake")
    assert response.status_code == 200

#test:anomalies
def test_anomalies_endpoint():
    response = client.get("/api/anomalies")
    assert response.status_code == 200