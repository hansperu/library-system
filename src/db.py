from sqlalchemy import Engine
from sqlmodel import Session, create_engine
from .config import get_config

config = get_config()

MYSQL_USER = config.MYSQL_USER
MYSQL_PASSWORD = config.MYSQL_PASSWORD
MYSQL_HOST = config.MYSQL_HOST
MYSQL_PORT = config.MYSQL_PORT
MYSQL_DATABASE = config.MYSQL_DATABASE



def get_engine() -> Engine:
    db_url = f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DATABASE}"
    engine = create_engine(db_url, echo=True)

    return engine

def get_session() -> Session:
    engine = get_engine()
    session = Session(engine)
    return session