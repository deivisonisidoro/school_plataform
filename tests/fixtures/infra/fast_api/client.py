import pytest
from typing import Any, Generator, Union
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from src.infra.db.relational_db import get_db
from src.infra.fast_api.server import app


@pytest.fixture(scope="function")
def client(db_session: Session) -> Generator[TestClient, Any, None]:
    """
    FastAPI TestClient fixture.

    This fixture creates a TestClient instance for testing FastAPI endpoints.
    The TestClient is used to make requests to the FastAPI application during testing.

    Yields:
        Generator[TestClient, Any, None]: A TestClient instance for testing.

    """

    def _get_test_db():
        try:
            yield db_session
        finally:
            pass

    app.dependency_overrides[get_db] = _get_test_db
    with TestClient(app) as test_client:
        yield test_client
