from pydantic import BaseModel


class WeatherSchema(BaseModel):
    temperature: float
    windspeed: float


class FinanceSchema(BaseModel):
    base: str
    usd_rate: float
    eur_rate: float


class EarthquakeSchema(BaseModel):
    magnitude: float
    place: str