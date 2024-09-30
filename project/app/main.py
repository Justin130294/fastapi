# project/app/main.py
"""
# Run application
Run server with reloading on save: uvicorn app.main:app --reload
Run server without reloading: uvicorn app.main:app

# View documentation
Raw JSON: http://localhost:8000/openapi.json
Swagger UI: http://localhost:8000/docs
ReDoc: http://localhost:8000/redoc
"""

from fastapi import FastAPI, Depends
from app.config import get_settings, Settings

app = FastAPI()


@app.get("/ping")
async def pong(settings: Settings = Depends(get_settings)):
    return {
        "ping": "pong!",
        "environment": settings.environment,
        "testing": settings.testing,
    }
