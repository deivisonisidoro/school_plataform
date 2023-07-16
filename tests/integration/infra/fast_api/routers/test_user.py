from fastapi.testclient import TestClient


class TestUserEndpoint:
    """
    Test cases for user-related endpoints.

    This test class contains test cases for user-related endpoints in the FastAPI application.
    It uses the TestClient to make requests and verify the responses.

    """

    def test_create_user(self, client: TestClient):
        """
        Test the create_user endpoint.

        This test checks if the endpoint successfully creates a new user and returns the correct status code and response data.

        Parameters:
            client (TestClient): The TestClient instance to make requests.

        """
        user_data = {
            "email": "test@example.com",
            "name": "Test User",
            "password": "testpassword",
        }

        response = client.post("api/users/", json=user_data)

        assert response.status_code == 201

        assert "id" in response.json()
        assert response.json()["email"] == user_data["email"]
        assert response.json()["name"] == user_data["name"]
