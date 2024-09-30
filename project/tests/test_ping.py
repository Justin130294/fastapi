# project/tests/test_ping.py


def test_ping(test_app):
    # Tests should be written in 3 parts: Given, When, Then
    # Given: The state of the application before the test runs (this includes the setup code, fixtures, database state)
    # test_app

    # When: the behaviour that is being tested
    response = test_app.get("/ping")

    # Then: The expected outcome of the test
    assert response.status_code == 200
    assert response.json() == {"ping": "pong!", "environment": "dev", "testing": True}
