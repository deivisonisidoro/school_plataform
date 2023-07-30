from typing import Dict
from dataclasses import dataclass


@dataclass
class HttpRequest:
    """
    Represents an HTTP request.

    Attributes:
        header (Dict, optional): A dictionary containing the headers of the HTTP request.
        body (Dict, optional): A dictionary containing the body data of the HTTP request.
        query (Dict, optional): A dictionary containing the query parameters of the HTTP request.
    """

    header: Dict = None
    body: Dict = None
    query: Dict = None
