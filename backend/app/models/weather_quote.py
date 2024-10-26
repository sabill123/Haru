from sqlalchemy import Column, Integer, Float, String, DateTime
from ..database import Base
import datetime

class WeatherQuote(Base):
    __tablename__ = "weather_quotes"

    id = Column(Integer, primary_key=True, index=True)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    weather = Column(String, nullable=False)
    quote = Column(String, nullable=False)
    image_url = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)