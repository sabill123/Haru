from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class LocationRequest(BaseModel):
    latitude: float
    longitude: float

class WeatherQuoteResponse(BaseModel):
    weather: str
    quote: str
    image_url: str
    created_at: datetime