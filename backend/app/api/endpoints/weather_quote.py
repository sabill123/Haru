from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ...database import get_db
from ...schemas.weather_quote import LocationRequest, WeatherQuoteResponse
from ...services import weather_service, quote_service, image_service
from ...models.weather_quote import WeatherQuote

router = APIRouter()

@router.post("/weather-quote", response_model=WeatherQuoteResponse)
async def get_weather_quote(
    request: LocationRequest,
    db: Session = Depends(get_db)
):
    try:
        # Get weather information
        weather = await weather_service.get_weather(
            request.latitude,
            request.longitude
        )
        
        # Generate quote
        quote = await quote_service.generate_quote(weather)
        
        # Generate image
        image_url = await image_service.generate_image(quote, weather)
        
        # Save to database
        db_weather_quote = WeatherQuote(
            latitude=request.latitude,
            longitude=request.longitude,
            weather=weather,
            quote=quote,
            image_url=image_url
        )
        db.add(db_weather_quote)
        db.commit()
        db.refresh(db_weather_quote)
        
        return WeatherQuoteResponse(
            weather=weather,
            quote=quote,
            image_url=image_url,
            created_at=db_weather_quote.created_at
        )
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))