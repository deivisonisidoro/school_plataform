import pytest
from fastapi.testclient import TestClient


class TestGetUserByEmailEndpoint:
    """
    Test cases for the GetUserByEmail endpoint.

    This class contains test cases for the GetUserByEmail endpoint, which allows fetching a user from the database
    based on their email.

    """

    @pytest.fixture
    def user_data(self):
        """
        Fixture that provides user data for testing.

        Returns:
            user_data (dict): User data in the format {"email": str, "name": str, "password": str}.
        """
        return {
            "email": "test@example.com",
            "name": "Test User",
            "password": "testpassword",
        }

    @pytest.fixture(autouse=True)
    def setup_and_teardown(self, client: TestClient, user_data):
        """
        Fixture that sets up and tears down the test database.

        This fixture creates a user before each test and clears the test database after each test.

        Args:
            client (TestClient): FastAPI TestClient instance.
            user_data (dict): User data to create the user in the database.
        """
        client.post("/api/users/", json=user_data)
        yield
        client.delete("/api/users/", params={"email": user_data["email"]})

    def test_get_user_found(self, client: TestClient, user_data: dict):
        """
        Test fetching a user by email when the user is found in the database.

        This test case verifies that the endpoint returns a status code of 200 (OK) when a user with the given
        email is found in the database.

        Args:
            client (TestClient): FastAPI TestClient instance.
            user_data (dict): User data used for the test.
        """
        get_user_response = client.get(f"/api/users/{user_data['email']}")
        assert get_user_response.status_code == 200

    def test_get_user_not_found(self, client: TestClient):
        """
        Test fetching a user by email when the user is not found in the database.

        This test case verifies that the endpoint returns a status code of 404 (Not Found) when a user with the given
        email is not found in the database.

        Args:
            client (TestClient): FastAPI TestClient instance.
        """
        non_existent_email = "nonexistent@example.com"
        response = client.get(f"/api/users/{non_existent_email}")
        assert response.status_code == 404
