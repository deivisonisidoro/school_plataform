from dataclasses import dataclass


@dataclass
class HttpResponse:
    """
    Represents an HTTP response.

    Attributes:
        status_code (int): The HTTP status code of the response.
        body (any): The response body, which can be of any data type.
    """

    status_code: int
    body: any
