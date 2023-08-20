import pytest
from pytest_mock import MockerFixture

from src.applications.dtos.user import UserDTO
from src.applications.use_cases.user.create_user import CreateUserUseCase
from src.domain.repositories.user import UserRepositoryInterface
from src.domain.use_cases.user.create_user import CreateUserUseCaseInterface
from src.infra.db.settings.connection import DBConnectionHandler
from src.infra.repositories.user import UserRepository
from src.domain.controller import ControllerInterface
from src.presenters.controllers.user.create_user import CreateUserController
from src.presenters.helpers.http_types import HttpRequest, HttpErrors


class TestCreateUserController:
    """
    Test suite for creating a new user via CreateUserController.
    """

    @pytest.fixture
    def user_dto(self) -> UserDTO:
        """
        Fixture that returns a sample UserDTO instance for testing.

        Returns:
            UserDTO: A UserDTO instance representing a sample user.
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
            user_repository (UserRepositoryInterface0: A mocked instance of the UserRepository.
        """
        user_repository = mocker.Mock(spec=UserRepository(db_connection=db_connection))
        return user_repository

    @pytest.fixture
    def create_user_use_case(
        self,
        user_repository: UserRepositoryInterface,
        mocker: MockerFixture,
    ) -> CreateUserUseCaseInterface:
        """
        Fixture that sets up the CreateUserUseCase with a mocked UserRepository.

        Args:
            user_repository (UserRepositoryInterface): The UserRepository fixture.

        Returns:
            CreateUserUseCaseInterface: An instance of CreateUserUseCase with the mock UserRepository.
        """
        create_user_use_case = mocker.Mock(CreateUserUseCase(user_repository=user_repository))
        return create_user_use_case

    @pytest.fixture
    def create_user_controller(self, create_user_use_case: CreateUserUseCaseInterface) -> ControllerInterface:
        """
        Fixture that sets up CreateUserController for testing.

        Args:
            create_user_use_case (CreateUserUseCaseInterface): The CreateUserUseCase fixture.

        Returns:
            create_user_controller (ControllerInterface): An instance of CreateUserController.
        """
        create_user_controller = CreateUserController(create_user_use_case=create_user_use_case)
        return create_user_controller

    def test_route_create_user(self, create_user_controller: CreateUserController, user_dto: UserDTO):
        """
        Test the route to create a new user.

        Args:
            create_user_controller (CreateUserController): The CreateUserController fixture.
            user_dto (UserDTO): The UserDTO fixture.
        """
        user_dict = user_dto.__dict__
        http_request = HttpRequest(body=user_dict)
        create_user_controller.create_user_use_case.create_user.return_value = {
            "data": user_dto,
            "success": True,
        }
        response = create_user_controller.route(http_request=http_request)
        assert response.status_code == 201
        assert response.body == user_dto

    def test_route_when_body_params_are_not_passed(self, create_user_controller: ControllerInterface):
        """
        Test that the route method of CreateUserController handles missing body parameters correctly.

        Args:
            create_user_controller (ControllerInterface): The CreateUserController fixture.
        """
        http_request = HttpRequest(body={"test": "create_user"})
        create_user_controller.create_user_use_case.create_user.return_value = None
        response = create_user_controller.route(http_request=http_request)

        assert response.status_code == HttpErrors.error_422()["status_code"]
        assert response.body == HttpErrors.error_422()["body"]
