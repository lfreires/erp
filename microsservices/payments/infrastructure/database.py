import os
from pathlib import Path
from dotenv import load_dotenv
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from models import Base

load_dotenv()

DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DB_POOL_SIZE = int(os.getenv("DB_POOL_SIZE", 10))
DB_MAX_OVERFLOW = int(os.getenv("DB_MAX_OVERFLOW", 20))
DB_POOL_RECYCLE = int(os.getenv("DB_POOL_RECYCLE", 3600))

BASE_URL = f"mysql+pymysql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/"

def create_database(db_name: str) -> None:
    """
    Cria o database/schema no MySQL se ainda não existir.
    """
    engine = create_engine(BASE_URL, pool_pre_ping=True)
    with engine.connect() as conn:
        conn.execute(
            text(f"CREATE DATABASE IF NOT EXISTS `{db_name}` "
                 "CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci")
        )
    engine.dispose()

def get_engine(db_name: str = DB_NAME):
    """
    Retorna um engine já apontando para o database desejado.
    """
    url = f"{BASE_URL}{db_name}"
    return create_engine(
        url,
        pool_pre_ping=True,
        pool_size=DB_POOL_SIZE,
        max_overflow=DB_MAX_OVERFLOW,
        pool_recycle=DB_POOL_RECYCLE,
    )

engine = get_engine()
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def init_db(db_name: str = DB_NAME):
    """
    Garante que o database exista e então cria todas as tabelas.
    """
    create_database(db_name)

    Base.metadata.create_all(bind=get_engine(db_name))

def get_db():
    """
    Dependency para FastAPI / scripts: gera e fecha sessão.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
