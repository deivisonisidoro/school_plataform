class HttpSuccess:
    """
    A collection of static methods representing common HTTP success responses.
    """

    @staticmethod
    def success_200(data=None):
        """
        Returns a dictionary representing an HTTP 200 OK success response.

        Args:
            data (Any, optional): The data to include in the response body. Defaults to None.

        Returns:
           ( Dict[str, Union[int, Any]]): The HTTP success response with 'status_code' and 'body' keys.
                The 'status_code' key contains the HTTP status code 200, and the 'body' key contains
                the provided data.
        """
        return {"status_code": 200, "body": data}

    @staticmethod
    def success_201(data=None):
        """
        Returns a dictionary representing an HTTP 201 Created success response.

        Args:
            data (Any, optional): The data to include in the response body. Defaults to None.

        Returns:
           ( Dict[str, Union[int, Any]]): The HTTP success response with 'status_code' and 'body' keys.
                The 'status_code' key contains the HTTP status code 201, and the 'body' key contains
                the provided data.
        """
        return {"status_code": 201, "body": data}
