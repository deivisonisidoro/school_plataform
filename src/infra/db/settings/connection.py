import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

load_dotenv()


class DBConnectionHandler:
    """Database connection handler for managing SQLAlchemy sessions.

    This class provides a context manager for managing database sessions using SQLAlchemy.
    It initializes a database engine based on the provided connection string from environment variables.

    Attributes:
        session: The current database session.

    Methods:
        get_engine(): Get the underlying SQLAlchemy database engine.
    """

    def __init__(self, connection_string: str = os.getenv("SQLALCHEMY_DATABASE_URL")) -> None:
        """Initialize a new instance of DBConnectionHandler."""
        self.connection_string = connection_string
        self.engine = self.__create_database_engine()
        self.session = None

    def __create_database_engine(self):
        """Create a new SQLAlchemy database engine.

        Returns:
            Engine: The created SQLAlchemy engine.
        """
        engine = create_engine(self.connection_string)
        return engine

    def get_engine(self):
        """Get the underlying SQLAlchemy database engine.

        Returns:
            Engine: The SQLAlchemy database engine.
        """
        return self.engine

    def __enter__(self):
        """Enter method for context management.

        Returns:
            DBConnectionHandler: This instance.
        """
        session_make = sessionmaker(bind=self.engine)
        self.session = session_make()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Exit method for context management.

        Args:
            exc_type: The exception type, if any.
            exc_val: The exception value, if any.
            exc_tb: The exception traceback, if any.
        """
        self.session.close()
