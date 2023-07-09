from sqlalchemy.orm import Session
from src.infra.db.relational_db import Base, DBConnectionHandler


class TestDBConnectionHandler:
    """
    Test class for DBConnectionHandler.
    """

    def test_create_db(self):
        # Initialize the DBConnectionHandler
        db_handler = DBConnectionHandler()

        # Call the create_db method
        db_handler.create_db()

        # Assert that the tables are created
        assert len(Base.metadata.tables) > 0

    def test_get_db(self):
        """
        Test the get_db method of DBConnectionHandler.

        This test initializes a DBConnectionHandler instance, uses the get_db method as a context manager,
        and asserts that the session obtained is an instance of SQLAlchemy's Session class.
        """
        db_handler = DBConnectionHandler()
        with db_handler.get_db() as session:
            assert isinstance(session, Session)
