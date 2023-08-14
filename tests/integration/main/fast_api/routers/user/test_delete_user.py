import pytest
from fastapi.testclient import TestClient

from src.applications.enums.user.success import UserSuccessEnum


class TestDeleteUserByEmailEndpoint:
    """
    Test cases for the deleteUserByEmail endpoint.

    This class contains test cases for the deleteUserByEmail endpoint, which allows fetching a user from the database
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

    @pytest.fixture(autouse=False)
    def setup_and_teardown(self, client: TestClient, user_data):
        """
        Fixture that sets up and tears down the test database.

        This fixture creates a user before each test and clears the test database after each test.

        Args:
            client (TestClient): FastAPI TestClient instance.
            user_data (dict): User data to create the user in the database.
        """
        client.post("/api/users/", json=user_data)

    def test_delete_user_found(self, client: TestClient, user_data: dict):
        """


        Args:
            client (TestClient): FastAPI TestClient instance.
            user_data (dict): User data used for the test.
        """
        client.post("/api/users/", json=user_data)
        create_user_response = client.get(f"/api/users/?email={user_data['email']}")
        user_id = create_user_response.json()["attributes"]["id"]
        response = client.delete(f"/api/users/{user_id}")
        assert response.status_code == 200
        assert response.json()["detail"] == UserSuccessEnum.DELETE_SUCCESS.value

    def test_delete_user_not_found(self, client: TestClient):
        """
        Test fetching a user by email when the user is not found in the database.

        This test case verifies that the endpoint returns a status code of 404 (Not Found) when a user with the given
        email is not found in the database.

        Args:
            client (TestClient): FastAPI TestClient instance.
        """
        non_existent_id = 999
        response = client.delete(f"/api/users/{non_existent_id}")
        assert response.status_code == 400
