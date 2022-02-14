import os, datetime
from dotenv import load_dotenv

load_dotenv(os.path.abspath(".env"))
baseDir = os.path.abspath("task_manager")


# Configurations For Application
class BaseConfig:
    """
    BaseConfig class contains all the basic configuration which are
    required for Development, Testing & Production phases of application
    """

    FLASK_ENV = "production"

    SECRET_KEY = os.environ.get("SECRET_KEY")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    RECAPTCHA_PUBLIC_KEY = os.environ.get("RECAPTCHA_PUBLIC_KEY")
    RECAPTCHA_PRIVATE_KEY = os.environ.get("RECAPTCHA_PRIVATE_KEY")
    REMEMBER_COOKIE_DURATION = datetime.timedelta(133)


class DevConfig(BaseConfig):
    """
    DevConfig class contains configuration for application when
    it is in development phase.

    There are also some configuration which has been inherited from
    BaseConfig class

    @param: BaseConfig (class)
    """

    FLASK_ENV = "development"
    SQLALCHEMY_DATABASE_URI = os.environ.get("MYSQL_DB_URI") or os.environ.get("SQLITE_DB_URI")
