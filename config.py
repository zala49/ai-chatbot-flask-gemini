import os


class Config:
    """Base configuration."""

    STATIC_FOLDER = "static"
    TEMPLATES_FOLDER = "templates"
    SESSION_COOKIE_NAME = 'my_flask_session'
    PERMANENT_SESSION_LIFETIME = 3600 


class DevelopmentConfig(Config):
    DEBUG = True
    TESTING = False


class TestingConfig(Config):
    DEBUG = False
    TESTING = True


class ProductionConfig(Config):
    DEBUG = False
    TESTING = False

config_by_name = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "production": ProductionConfig,
    "default": DevelopmentConfig,
}
