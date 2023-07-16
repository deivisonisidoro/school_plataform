from fastapi.testclient import TestClient


class TestRedirectToDocumentation:
    """
    Test cases for the Redirect to Documentation endpoint.

    This test class contains test cases for the `/` endpoint that redirects to the Swagger API documentation page.
    It uses the TestClient to make requests and check the response status and headers.

    """

    def test_redirect_endpoint_status_code(self, client: TestClient):
        """
        Test the status code of the / endpoint.

        This test checks if the endpoint returns a 302 status code, indicating a redirect.

        Parameters:
            client (TestClient): The TestClient instance to make requests.

        """
        response = client.get("/")
        assert response.status_code == 200
