# Logging configuration
import logging
from logging.handlers import RotatingFileHandler
import os

LOG_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'logs')
os.makedirs(LOG_DIR, exist_ok=True)
LOG_FILE = os.path.join(LOG_DIR, 'app.log')

LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')

def setup_logging():
    logger = logging.getLogger()
    logger.setLevel(LOG_LEVEL)

    formatter = logging.Formatter('[%(asctime)s] %(levelname)s in %(module)s: %(message)s')

    # Console handler
    ch = logging.StreamHandler()
    ch.setLevel(LOG_LEVEL)
    ch.setFormatter(formatter)
    logger.addHandler(ch)

    # Rotating file handler
    fh = RotatingFileHandler(LOG_FILE, maxBytes=1_000_000, backupCount=5)
    fh.setLevel(LOG_LEVEL)
    fh.setFormatter(formatter)
    logger.addHandler(fh)

    # Avoid duplicate logs if setup_logging is called multiple times
    logger.propagate = False

# Call setup_logging at import
setup_logging()
from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict
import os



# Determine environment (default to 'dev')
env = os.getenv("ENV", "dev").lower()
env_file = f".env.{env}"

class Settings(BaseSettings):
    app_name: str = "SpendSense"
    debug: bool = False
    database_url: str = ''
    database_connection_args: dict = {"check_same_thread": False}

    model_config = SettingsConfigDict(env_file=env_file, env_file_encoding="utf-8")

@lru_cache()
def get_settings():
    return Settings()
