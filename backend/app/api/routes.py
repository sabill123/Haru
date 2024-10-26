from fastapi import APIRouter
from .endpoints import weather_quote

api_router = APIRouter()
api_router.include_router(weather_quote.router, prefix="/api")