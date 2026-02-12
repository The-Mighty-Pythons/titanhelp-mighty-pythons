import os

class DevConfig:
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite:///titanhelp.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
