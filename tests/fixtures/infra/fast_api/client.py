import pytest
from typing import Any, Generator
from fastapi.testclient import TestClient

from src.infra.db.settings.connection import DBConnectionHandler
from src.main.fast_api.configs.server import app


@pytest.fixture(scope="function")
def client(db_connection: DBConnectionHandler) -> Generator[TestClient, Any, None]:
    """
    FastAPI TestClient fixture.

    This fixture creates a TestClient instance for testing FastAPI endpoints.
    The TestClient is used to make requests to the FastAPI application during testing.

    Args:
        db_connection (DBConnectionHandler): A database connection handler for the test database.

    Yields:
        Generator[TestClient, Any, None]: A TestClient instance for testing.

    """

    def _get_test_db():
        try:
            yield db_connection.session
        finally:
            pass

    app.dependency_overrides[db_connection.session] = _get_test_db
    with TestClient(app) as test_client:
        yield test_client
