# project/tests/conftest.py

import os

import pytest
from starlette.testclient import TestClient
from tortoise.contrib.fastapi import register_tortoise

from app.config import Settings, get_settings
from app.main import create_application


def get_settings_override():
    return Settings(testing=1, database_url=os.environ.get("DATABASE_TEST_URL"))


# pytest fixtures are reusable objects for tests. They have a scope parameter that can be set to
# function, class, module, package, or session. The default scope is function. The scope parameter
# indicates how often the fixture is invoked.
# function - once per test function (default)
# class - once per test class
# module - once per module
# session - once per test session
@pytest.fixture(scope="module")
def test_app():
    # Create application
    app = create_application()

    # Override dependencies; get_settings is the key in the dependency_overrides dictionary
    app.dependency_overrides[get_settings] = get_settings_override

    # Use the Starlette TestClient to make requests against the FastAPI application
    with TestClient(app) as test_client:
        # testing; all code before the yield statement serves as setup code while everything
        # after serves as teardown code
        yield test_client

    # tear down


@pytest.fixture(scope="module")
def test_app_with_db():
    # set up
    app = create_application()
    app.dependency_overrides[get_settings] = get_settings_override
    register_tortoise(
        app,
        db_url=os.environ.get("DATABASE_TEST_URL"),
        modules={"models": ["app.models.tortoise"]},
        generate_schemas=True,
        add_exception_handlers=True,
    )

    with TestClient(app) as test_client:
        # testing
        yield test_client
