import os
from flask import Flask
from config import CONFIG_BY_NAME
from .extensions import db
from .routes import bp as main_bp

def create_app(config_name: str | None = None) -> Flask:
    app = Flask(__name__)

    env_name = (
        config_name
        or os.getenv("APP_ENV")
        or os.getenv("FLASK_ENV")
        or "development"
    )

    config_class = CONFIG_BY_NAME.get(env_name, CONFIG_BY_NAME["development"])
    app.config.from_object(config_class)

    db.init_app(app)
    app.register_blueprint(main_bp)

    return app
