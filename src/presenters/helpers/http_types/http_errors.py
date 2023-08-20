class HttpErrors:
    """
    A collection of static methods representing common HTTP error responses.
    """

    @staticmethod
    def error_422():
        """
        Returns a dictionary representing an HTTP 422 Unprocessable Entity error response.

        Returns:
            (Dict[str, Union[int, Dict[str, str]]]): The HTTP error response with 'status_code' and 'body' keys.
                The 'status_code' key contains the HTTP status code 422, and the 'body' key contains
                an error message for Unprocessable Entity.
        """
        return {"status_code": 422, "body": {"error": "Unprocessable Entity"}}

    @staticmethod
    def error_400():
        """
        Returns a dictionary representing an HTTP 400 Bad Request error response.

        Returns:
            (Dict[str, Union[int, Dict[str, str]]]): The HTTP error response with 'status_code' and 'body' keys.
                The 'status_code' key contains the HTTP status code 400, and the 'body' key contains
                an error message for Bad Request.
        """
        return {"status_code": 400, "body": {"error": "Bad Request"}}

    @staticmethod
    def error_404():
        """
        Returns a dictionary representing an HTTP 404 Not Found error response.

        Returns:
            (Dict[str, Union[int, Dict[str, str]]]): The HTTP error response with 'status_code' and 'body' keys.
                The 'status_code' key contains the HTTP status code 404, and the 'body' key contains
                an error message for Not Found.
        """
        return {"status_code": 404, "body": {"error": "Not Found"}}
