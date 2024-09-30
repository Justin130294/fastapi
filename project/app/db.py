# project/app/db.py

# Add tortoise config (for aerich migrations)

import logging
import os

from fastapi import FastAPI
from tortoise import Tortoise, run_async
from tortoise.contrib.fastapi import register_tortoise

log = logging.getLogger("uvicorn")

TORTOISE_ORM = {
    "connections": {"default": os.getenv("DATABASE_URL")},
    "apps": {
        "models": {
            "models": ["app.models.tortoise", "aerich.models"],
            "default_connection": "default",
        }
    },
}


def init_db(app: FastAPI) -> None:
    # Set up Tortoise on startup and clean up on teardown
    register_tortoise(
        app,
        db_url=os.getenv("DATABASE_URL"),
        modules={"models": ["app.models.tortoise"]},
        generate_schemas=False,  # Do not create tables on startup since using Aerich to manage schema
        add_exception_handlers=True,
    )


# Function to set up Tortoise ORM and then generate schema
async def generate_schema() -> None:
    log.info("Initializing Tortoise...")

    await Tortoise.init(
        db_url=os.getenv("DATABASE_URL"), modules={"models": ["models.tortoise"]}
    )

    log.info("Generating database schema via Tortoise...")
    await Tortoise.generate_schemas()
    await Tortoise.close_connections()


if __name__ == "__main__":
    run_async(generate_schema())
