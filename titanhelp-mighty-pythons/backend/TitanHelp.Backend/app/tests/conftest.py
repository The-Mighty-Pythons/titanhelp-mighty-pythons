## this file is used to make all tests available to pytest, and to set up fixtures for testing
## this file will be used for
##    app, client, db_Session, sample_ticket and ticket_factory

import pytest
from app import create_app
from app.extensions import db


@pytest.fixture(scope="function")
def app():
    # Create a new Flask app instance for testing
    app = create_app(
        {
            # Override config for testing to use in-memory SQLite database instead of the acutal database
            "TESTING": True,
            "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:",
            "SQLALCHEMY_TRACK_MODIFICATIONS": False,
        }
    )

    with app.app_context():
        # Guardrail
        assert app.config["SQLALCHEMY_DATABASE_URI"] == "sqlite:///:memory:"

        db.create_all()
        try:
            yield app
        finally:
            # Always clean up, even if the test fails.
            db.session.remove()
            db.drop_all()


@pytest.fixture(scope="function")
def client(app):
    # Flask test client for exercising the API endpoints
    return app.test_client()