from dataclasses import dataclass

from src.domain.use_cases.user.get_user import GetUserUseCaseInterface
from src.presenters.errors import HttpErrors
from src.presenters.helpers.http_types import HttpRequest, HttpResponse
from src.main.interfaces import RouteInterface


@dataclass
class GetUserController(RouteInterface):
    """
    Represents a controller for handling HTTP requests related to retrieving user data.

    Args:
        get_user_use_case (GetUserUseCaseInterface): An instance of GetUserUseCaseInterface that provides
            the necessary functionality to fetch user data.

    Returns:
        HttpResponse: An HTTP response object containing the result of the user retrieval operation.
    """

    get_user_use_case: GetUserUseCaseInterface

    def route(self, http_request: HttpRequest) -> HttpResponse:
        """
        Handle the HTTP request to retrieve user data.

        Args:
            http_request (HttpRequest): An HTTP request object containing the request data.

        Returns:
            HttpResponse: An HTTP response object containing the result of the user retrieval operation.
                If successful, it contains a status code 200 and the user data in the 'body'.
                If the user is not found or any error occurs during retrieval, it returns an appropriate
                error response with the corresponding status code and error message in the 'body'.
        """
        response = None
        if http_request.query:
            query_string_params = http_request.query.keys()
            if "email" in query_string_params:
                email = http_request.query["email"]
                response = self.get_user_use_case.get_user_by_email(email=email)
            else:
                response = {"success": False, "data": None}
            if response["success"] is False:
                http_error = HttpErrors.error_422()
                return HttpResponse(status_code=http_error["status_code"], body=http_error["body"])

            return HttpResponse(status_code=response["status_code"], body=response["data"])

        http_error = HttpErrors.error_400()
        return HttpResponse(status_code=http_error["status_code"], body=http_error["body"])
