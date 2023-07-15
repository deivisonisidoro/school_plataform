import os
import sys
from typing import Any, Generator
from contextlib import contextmanager
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

from src.infra.db.relational_db.declarative_base import Base

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionTesting = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@contextmanager
@pytest.fixture
def db_session() -> Generator[Session, Any, None]:
    """Fixture for creating a test database session.

    Yields:
        Session: The test database session.
    """
    session = SessionTesting()

    Base.metadata.create_all(bind=engine)

    try:
        yield session
    finally:
        session.close()
        session.rollback()
        Base.metadata.drop_all(bind=engine)
        engine.dispose()
        try:
            os.remove("test.db")
        except FileNotFoundError:
            pass


class TestDB:
    """Test class for database testing."""

    @classmethod
    def setup_class(cls):
        """Set up method called before starting the test class."""
        Base.metadata.create_all(bind=engine)
        cls.Session = sessionmaker(bind=engine)

    @classmethod
    def teardown_class(cls):
        """Teardown method called after completing the test class."""
        Base.metadata.drop_all(bind=engine)
