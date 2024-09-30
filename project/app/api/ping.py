# project/app/api/ping.py

from fastapi import APIRouter, Depends

from app.config import Settings, get_settings

# Create a new FastAPI router mounted on the /api path
router = APIRouter()


@router.get("/ping")
async def pong(settings: Settings = Depends(get_settings)):
    return {
        "ping": "pong!",
        "environment": settings.environment,
        "testing": settings.testing,
    }
