## this file is used to make all tests available to pytest, and to set up fixtures for testing
## this file will be used for
##    app, client, db_Session, sample_ticket and ticket_factory

import pytest
from app import create_app
from app.extensions import db


@pytest.fixture(scope="function")
def app():
    app = create_app()

    # Override config for testing to use in-memory SQLite database instead of the acutal database
    app.config.update({
        "TESTING": True,
        "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:",
    })

    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()


@pytest.fixture(scope="function")
def client(app):
    return app.test_client()