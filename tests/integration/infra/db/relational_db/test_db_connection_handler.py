from src.infra.db.relational_db import Base, create_db


class TestDBConnectionHandler:
    """
    Test class for DBConnectionHandler.
    """

    def test_create_db(
        self,
    ):
        """Test the creation of the database.

        This test verifies if the database is successfully created.

        It checks if there are tables defined in the Base.metadata.tables.

        """

        create_db()

        assert len(Base.metadata.tables) > 0
