import pytest
from pytest_mock import MockerFixture

from src.applications.dtos.user import UserDTO
from src.applications.use_cases.user.delete_user_use_case import DeleteUserUseCase
from src.domain.enums.user.success import UserSuccessEnum
from src.domain.repositories.user import UserRepositoryInterface
from src.domain.use_cases.user.delete_user import DeleteUserUseCaseInterface
from src.infra.db.settings.connection import DBConnectionHandler
from src.infra.repositories.user import UserRepository
from src.main.interfaces.route import RouteInterface
from src.presenters.controllers.user.delete_user import DeleteUserController
from src.presenters.errors.http_errors import HttpErrors
from src.presenters.helpers.http_types.http_request import HttpRequest


class TestDeleteController:
    """
    Test suite for the DeleteUserController class.
    """

    @pytest.fixture
    def user_dto(self) -> UserDTO:
        """
        Fixture that returns a sample UserDTO instance for testing.

        Returns:
            UserDTO: A sample UserDTO instance representing a user.
        """
        user_dto = UserDTO(
            id=1,
            name="John Doe",
            email="johndoe@example.com",
            password="password123",
            created_at="2023-07-21 12:34:56",
        )
        return user_dto

    @pytest.fixture
    def user_repository(self, mocker: MockerFixture, db_connection: DBConnectionHandler) -> UserRepositoryInterface:
        """
        Fixture that sets up a mocked UserRepository with a sample user.

        Args:
            mocker (MockerFixture): Pytest-mock fixture for creating mock objects.
            db_connection (Session): SQLAlchemy session fixture.

        Returns:
            UserRepositoryInterface: A mocked instance of the UserRepository.
        """
        user_repository = mocker.Mock(spec=UserRepository(db_connection=db_connection))
        return user_repository

    @pytest.fixture
    def delete_user_use_case(
        self,
        user_repository: UserRepositoryInterface,
        mocker: MockerFixture,
    ) -> DeleteUserUseCaseInterface:
        """
        Fixture that sets up the DeleteUserUseCase with a mocked UserRepository.

        Args:
            user_repository (UserRepositoryInterface): The UserRepository fixture.

        Returns:
            DeleteUserUseCaseInterface: An instance of DeleteUserUseCase with the mock UserRepository.
        """
        delete_user_use_case = mocker.Mock(DeleteUserUseCase(user_repository=user_repository))
        return delete_user_use_case

    @pytest.fixture
    def delete_user_controller(self, delete_user_use_case: DeleteUserUseCaseInterface) -> RouteInterface:
        """
        Fixture that sets up DeleteUserController for testing.

        Args:
            delete_user_use_case (DeleteUserUseCaseInterface): The DeleteUserUseCase fixture.

        Returns:
            RouteInterface: An instance of DeleteUserController.
        """
        delete_user_controller = DeleteUserController(delete_user_use_case=delete_user_use_case)
        return delete_user_controller

    def test_route_delete_user_successful_deletion(
        self,
        delete_user_controller: RouteInterface,
        user_dto: UserDTO,
    ):
        """
        Test the route for deleting a user when the deletion is successful.

        Args:
            delete_user_controller (RouteInterface): An instance of DeleteUserController.
            user_dto (UserDTO): The UserDTO representing the user to be deleted.
        """
        http_request = HttpRequest(path={"user_id": user_dto.id})
        delete_user_controller.delete_user_use_case.delete_user.return_value = {
            "data": UserSuccessEnum.DELETE_SUCCESS.value,
            "success": True,
        }

        response = delete_user_controller.route(http_request=http_request)

        assert response.status_code == 200
        assert response.body == UserSuccessEnum.DELETE_SUCCESS.value

    def test_route_path_not_passed(self, delete_user_controller: RouteInterface):
        """
        Test the route behavior when the path is not passed.

        Args:
            delete_user_controller (RouteInterface): An instance of DeleteUserController.
        """

        http_request = HttpRequest(path={"test": "test"})
        http_error = HttpErrors.error_422()
        delete_user_controller.delete_user_use_case.delete_user.return_value = {
            "success": False,
            "data": http_error["body"],
            "status_code": http_error["status_code"],
        }

        response = delete_user_controller.route(http_request=http_request)

        assert response.status_code == http_error["status_code"]
        assert response.body == http_error["body"]

    def test_route_not_delete_user_user_not_exists(self, delete_user_controller: RouteInterface):
        """
        Test that the route does not delete a user when the user does not exist.

        Args:
            delete_user_controller (RouteInterface): An instance of DeleteUserController.
        """

        http_request = HttpRequest(path={"user_id": "test@test.com"})
        http_error = HttpErrors.error_400()
        delete_user_controller.delete_user_use_case.delete_user.return_value = {
            "success": False,
            "data": http_error["body"],
            "status_code": http_error["status_code"],
        }

        response = delete_user_controller.route(http_request=http_request)

        assert response.status_code == http_error["status_code"]
        assert response.body == http_error["body"]
