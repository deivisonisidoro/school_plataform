import os
from typing import Generator
import pytest
from sqlalchemy.orm import Session, sessionmaker

from src.infra.db.settings import Base, DBConnectionHandler


@pytest.fixture
def db_connection() -> Generator[DBConnectionHandler, None, None]:
    """Fixture for creating a test database session.

    This fixture sets up a temporary SQLite database connection for testing purposes.
    A connection to the database is yielded, and after the test is finished, the connection
    is closed, and the temporary database file is removed.

    Yields:
        db_connection (DBConnectionHandler): A database connection handler for the test database.
    """
    connection_string = "sqlite:///./test.db"
    try:
        connection = DBConnectionHandler(connection_string=connection_string)
        Base.metadata.create_all(bind=connection.engine)
        yield connection
    finally:
        Base.metadata.drop_all(bind=connection.engine)
        try:
            os.remove("test.db")
        except FileNotFoundError:
            pass


class TestDB:
    """Test class for database testing."""

    @classmethod
    def setup_class(cls):
        """Set up method called before starting the test class."""
        cls.Session = sessionmaker()

    @classmethod
    def teardown_class(cls):
        """Teardown method called after completing the test class."""
        pass
