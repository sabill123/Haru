import httpx
from ..config import settings
from ..utils.exceptions import WeatherServiceException

async def get_weather(lat: float, lon: float) -> str:
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(
                f"https://api.openweathermap.org/data/2.5/weather",
                params={
                    "lat": lat,
                    "lon": lon,
                    "appid": settings.WEATHER_API_KEY,
                    "units": "metric",
                    "lang": "kr"
                }
            )
            data = response.json()
            temp = data["main"]["temp"]
            weather_desc = data["weather"][0]["description"]
            return f"기온: {temp}°C, 날씨: {weather_desc}"
    except Exception as e:
        raise WeatherServiceException(str(e))