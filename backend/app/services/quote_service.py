from openai import AsyncClient
from ..config import settings

async def generate_quote(weather: str) -> str:
    client = AsyncClient(api_key=settings.OPENAI_API_KEY)
    
    response = await client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "현재 날씨와 사회적 상황에 맞는 영감을 주는 명언을 한 문장으로 생성해주세요."
            },
            {
                "role": "user",
                "content": f"현재 날씨: {weather}"
            }
        ]
    )
    return response.choices[0].message.content