# project/app/main.py

import logging

from fastapi import FastAPI

from app.api import ping, summaries
from app.db import init_db

# Create a logger instance with the name uvicorn
log = logging.getLogger("uvicorn")


# Function to initialise application
def create_application() -> FastAPI:
    application = FastAPI()
    # Include the ping router
    application.include_router(ping.router)
    # Include the summaries router
    application.include_router(
        summaries.router, prefix="/summaries", tags=["summaries"]
    )

    return application


app = create_application()  # Create the FastAPI application


@app.on_event("startup")
async def startup_event():
    log.info("Starting up...")
    init_db(app)


@app.on_event("shutdown")
async def shutdown_event():
    log.info("Shutting down...")
