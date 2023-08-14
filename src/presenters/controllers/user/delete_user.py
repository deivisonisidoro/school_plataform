from dataclasses import dataclass

from src.domain.use_cases.user.delete_user import DeleteUserUseCaseInterface
from src.presenters.errors import HttpErrors
from src.presenters.helpers.http_types import HttpRequest, HttpResponse
from src.domain.controllers import ControllerInterface
from src.presenters.success.http_success import HttpSuccess


@dataclass
class DeleteUserController(ControllerInterface):
    """
    Represents a controller for handling HTTP requests related to retrieving user data.

    Args:
        delete_user_use_case (DeleteUserUseCaseInterface): An instance of DeleteUserUseCaseInterface that provides
            the necessary functionality to fetch user data.

    Returns:
        HttpResponse: An HTTP response object containing the result of the user retrieval operation.
    """

    delete_user_use_case: DeleteUserUseCaseInterface

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
        if http_request.path:
            path_string_params = http_request.path.keys()
            if "user_id" in path_string_params:
                user_id = http_request.path["user_id"]
                response = self.delete_user_use_case.delete_user(user_id=user_id)
            else:
                http_error = HttpErrors.error_422()
                response = {"success": False, "data": http_error["body"], "status_code": http_error["status_code"]}
                return HttpResponse(status_code=http_error["status_code"], body=http_error["body"])
            if response["success"] is False:
                http_error = HttpErrors.error_400()
                return HttpResponse(status_code=http_error["status_code"], body=response["data"])
            http_success = HttpSuccess.success_200(data=response["data"])
            return HttpResponse(status_code=http_success["status_code"], body=http_success["body"])
