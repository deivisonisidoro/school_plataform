from dataclasses import dataclass

from src.applications.dtos.user import UserDTO
from src.domain.use_cases.user.create_user import CreateUserUseCaseInterface
from src.domain.controllers.controller import ControllerInterface
from src.presenters.helpers.http_types import HttpRequest, HttpResponse, HttpErrors, HttpSuccess


@dataclass
class CreateUserController(ControllerInterface):
    """
    A controller for creating new user accounts.

    This controller handles HTTP requests to create new user accounts.
    It utilizes the CreateUserUseCase to perform the creation process.

    Attributes:
        create_user_use_case (CreateUserUseCaseInterface): An instance of the CreateUserUseCaseInterface
            responsible for creating user accounts.
    """

    create_user_use_case: CreateUserUseCaseInterface

    def route(self, http_request: HttpRequest) -> HttpResponse:
        """
        Handle the incoming HTTP request and create a new user account if the provided data is valid.

        Args:
            http_request (HttpRequest): The incoming HTTP request object.

        Returns:
            HttpResponse: An HTTP response indicating the outcome of the request.
        """
        response = None
        if http_request.body:
            body_params = http_request.body.keys()
            if "name" in body_params and "email" in body_params and "password" in body_params:
                user_dto = UserDTO(
                    id=None,
                    name=http_request.body["name"],
                    email=http_request.body["email"],
                    password=http_request.body["password"],
                    created_at=None,
                )
                response = self.create_user_use_case.create_user(user_dto=user_dto)
            else:
                http_error = HttpErrors.error_422()
                response = {"success": False, "data": http_error["body"], "status_code": http_error["status_code"]}
                return HttpResponse(status_code=http_error["status_code"], body=http_error["body"])
        if response["success"] is False:
            http_error = HttpErrors.error_400()
            return HttpResponse(status_code=http_error["status_code"], body=response["data"])
        http_success = HttpSuccess.success_201(data=response["data"])
        return HttpResponse(status_code=http_success["status_code"], body=http_success["body"])
