from sqlalchemy import Column, Integer, Float, String, DateTime
from datetime import datetime
from app.database import Base


class WeatherData(Base):
    __tablename__ = "weather_data"

    id = Column(Integer, primary_key=True, index=True)
    temperature = Column(Float)
    windspeed = Column(Float)
    timestamp = Column(DateTime, default=datetime.utcnow)


class FinanceData(Base):
    __tablename__ = "finance_data"

    id = Column(Integer, primary_key=True, index=True)
    base_currency = Column(String)
    usd_rate = Column(Float)
    eur_rate = Column(Float)
    timestamp = Column(DateTime, default=datetime.utcnow)


class EarthquakeData(Base):
    __tablename__ = "earthquake_data"

    id = Column(Integer, primary_key=True, index=True)
    magnitude = Column(Float)
    place = Column(String)
    timestamp = Column(DateTime, default=datetime.utcnow)


class AnomalyAlert(Base):
    __tablename__ = "anomaly_alerts"

    id = Column(Integer, primary_key=True, index=True)
    alert_type = Column(String)
    message = Column(String)
    timestamp = Column(DateTime, default=datetime.utcnow)