from sqlmodel import SQLModel, create_engine, Session
from config import get_settings
import logging as log

try:
    log.info("Creating database engine")
    settings = get_settings()
    engine = create_engine(settings.database_url, echo=settings.debug)
except Exception as e:
    log.error("Error creating database engine: %s", e)
    raise

def get_session():
    with Session(engine) as session:
        yield session

# Usage example:
# db = Database()
# with db.get_session() as session:
#     ... # use session
