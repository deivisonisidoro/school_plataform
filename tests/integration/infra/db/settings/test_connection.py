from src.infra.db.settings import DBConnectionHandler


class TestDatabaseConnection:
    """
    Test class for the database connection.

    This class contains tests to verify the creation of the database engine
    using the DBConnectionHandler class.
    """

    def test_create_database_engine(self):
        """
        Test the creation of the database engine.

        This test checks if the database engine is created correctly
        using the DBConnectionHandler class.

        The test will fail if the engine is not created or is created inadequately
        """
        db_connection_handle = DBConnectionHandler()

        engine = db_connection_handle.get_engine()

        assert engine is not None
