import httpx

USER_SERVICE_URL = "http://localhost:8000/users"

async def validate_user(user_id: str) -> bool:
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(f"{USER_SERVICE_URL}/{user_id}")
            return response.status_code == 200
    except httpx.RequestError:
        return False
