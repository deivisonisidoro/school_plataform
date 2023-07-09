from sqlalchemy.orm import Session

from sqlalchemy.orm import sessionmaker

from sqlalchemy import create_engine

from contextlib import contextmanager

from .declarative_base import Base


class DBConnectionHandler:
    def __init__(self, connection_string: str = "sqlite:///:memory:"):
        self.engine = create_engine(connection_string)

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
