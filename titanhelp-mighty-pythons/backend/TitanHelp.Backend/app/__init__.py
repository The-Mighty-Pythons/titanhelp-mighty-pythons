from flask import Flask, jsonify
from flask_cors import CORS
from dotenv import load_dotenv

from .config import DevConfig
from .extensions import db

def create_app(test_config: dict | None = None):
    load_dotenv()

    app = Flask(__name__)
    app.config.from_object(DevConfig)

    if test_config:
        app.config.update(test_config)

    db.init_app(app)

    # Ensure models are imported before creating tables
    from . import models # noqa: F401

    CORS(app, resources={r"/api/*": {"origins": "*"}})

    from .api.tickets_controller import tickets_bp
    app.register_blueprint(tickets_bp, url_prefix="/api")

    return app