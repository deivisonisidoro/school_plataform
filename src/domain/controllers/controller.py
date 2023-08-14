from abc import ABC, abstractmethod
from src.presenters.helpers.http_types import HttpRequest, HttpResponse


class ControllerInterface(ABC):
    """Interface for defining a route."""

    @abstractmethod
    def route(self, http_request: HttpRequest) -> HttpResponse:
        """Route the HTTP request and return the corresponding HTTP response.

        Args:
            http_request (HttpRequest): The incoming HTTP request.

        Returns:
            HttpResponse: The generated HTTP response.
        """
