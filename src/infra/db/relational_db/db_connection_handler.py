import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .declarative_base import Base
from dotenv import load_dotenv

load_dotenv()

SQLALCHEMY_DATABASE_URL = os.getenv("SQLALCHEMY_DATABASE_URL")

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def create_db():
    """
    Create all database tables.

    This function creates all database tables defined in the models.py file, based on the metadata created by the declarative base.

    """
    Base.metadata.create_all(bind=engine)


def get_db():
    """
    Get a database session.

    This function returns a context manager that provides a SQLAlchemy session. The session is closed automatically when the context manager is exited.

    Returns:
        generator: A generator that yields a database session.

    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
