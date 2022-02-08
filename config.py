import os, secrets


class BaseConfig:
    """
    BaseConfig class contains basic Configuration for
    Development, Testing & Production mode
    """

    FLASK_ENV = "production"

    SECRET_KEY = os.environ.get("SECRET_KEY")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    RECAPTCHA_PUBLIC_KEY = os.environ.get("RECAPTCHA_PUBLIC_KEY")
    RECAPTCHA_PRIVATE_KEY = os.environ.get("RECAPTCHA_PRIVATE_KEY")


class DevConfig(BaseConfig):
    FLASK_ENV = "development"
