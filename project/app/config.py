# project/app/config.py

"""
File to define environment specific configuration variables
"""

import logging
from functools import lru_cache
from pydantic_settings import BaseSettings

log = logging.getLogger("uvicorn")


class Settings(BaseSettings):
    environment: str = "dev"
    testing: bool = False


# Cache the dependency function so it is not executed every time it is requested
@lru_cache()
def get_settings() -> BaseSettings:
    log.info("Loading config settings from the environment...")
    return Settings()
