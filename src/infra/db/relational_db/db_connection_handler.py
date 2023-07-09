from sqlalchemy.orm import Session
from contextlib import contextmanager
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

from .declarative_base import Base


class DBConnectionHandler:
    """
    Handles the database connection and session management.
    """

    def __init__(
        self,
        connection_string: str = "sqlite:///:memory:",
        base: Base = Base,
    ):
        """
        Initialize the DBConnectionHandler.

        Args:
            connection_string (str, optional): The database connection string. Defaults to "sqlite:///:memory:".
            base (Base, optional): The SQLAlchemy declarative base class. Defaults to Base.
        """
        self.engine = create_engine(connection_string)
        self.base = base

    def create_db(self):
        """
        Create all database tables.

        This function creates all database tables defined in the models.py file, based on the metadata created by the declarative base.

        """
        self.base.metadata.create_all(bind=self.engine)

    @contextmanager
    def get_db(self) -> Session:
        """
        Get a database session.

        This function returns a SQLAlchemy session object.

        Yields:
            Session: A SQLAlchemy session object.
        """
        session_local = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)
        db = session_local()
        try:
            yield db
        finally:
            db.close()
