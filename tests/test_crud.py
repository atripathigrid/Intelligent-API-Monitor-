from app.schemas import WeatherSchema
from app.crud import create_weather

#Fake DB
class FakeDB:
    def add(self, obj):
        pass

    def commit(self):
        pass

    def refresh(self, obj):
        pass

#test function
def test_create_weather():
    db = FakeDB()

    weather = WeatherSchema(
        temperature=30,
        windspeed=12
    )

    result = create_weather(db, weather)

    assert result.temperature == 30
    assert result.windspeed == 12