import pytest
from fastapi.testclient import TestClient


@pytest.mark.skip(reason="Test connected with local bd, and not with test bd")
class TestCreateUserEndpoint:
    """
    Test cases for user-related endpoints.

    This test class contains test cases for user-related endpoints in the FastAPI application.
    It uses the TestClient to make requests and verify the responses.

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

    def test_create_user(self, client: TestClient, user_data: dict):
        """
        Test the create_user endpoint.

        This test checks if the endpoint successfully creates a new user and returns the correct status code and response data.

        Parameters:
            client (TestClient): The TestClient instance to make requests.
            user_data (dict): User data for creating a new user in the request body.

        """
        response = client.post("api/users/", json=user_data)

        assert response.status_code == 201

    def test_create_user_when_user_already_exist(self, client: TestClient, user_data: dict):
        """
        Test the create_user endpoint when the user already exists.

        This test checks if the endpoint correctly handles the case when a user with the same email already exists,
        and returns the appropriate status code and error response.

        Parameters:
            client (TestClient): The TestClient instance to make requests.
            user_data (dict): User data for creating a new user in the request body.

        """
        client.post("api/users/", json=user_data)
        response = client.post("api/users/", json=user_data)

        assert response.status_code == 400
