from openai import AsyncClient
from ..config import settings

async def generate_image(quote: str, weather: str) -> str:
    client = AsyncClient(api_key=settings.OPENAI_API_KEY)
    
    response = await client.images.generate(
        model="dall-e-3",
        prompt=f"Generate an inspiring image that matches this quote and weather: {quote}, {weather}",
        size="1024x1024",
        quality="standard",
        n=1,
    )
    return response.data[0].url