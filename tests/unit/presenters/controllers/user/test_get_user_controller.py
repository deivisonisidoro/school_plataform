import pytest
from pytest_mock import MockerFixture
from sqlalchemy.orm import Session

from src.applications.dtos.user import UserDTO
from src.applications.use_cases.user.get_user_by_email import GetUserUseCase
from src.domain.use_cases.user.create_user import CreateUserUseCaseInterface
from src.domain.use_cases.user.get_user import GetUserUseCaseInterface
from src.domain.repositories.user import UserRepositoryInterface
from src.infra.repositories.user import UserRepository
from src.presenters.errors.http_errors import HttpErrors
from src.presenters.controllers.user.get_user_controller import GetUserController
from src.presenters.helpers.http_types import HttpRequest


class TestGetUserController:
    """
    Test suite for GetUserController.

    Attributes:
        user_dto (UserDTO): A sample UserDTO instance for testing.
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
    def user_repository(self, mocker: MockerFixture, db_session: Session) -> UserRepositoryInterface:
        """
        Fixture that sets up a mocked UserRepository with a sample user.

        Args:
            mocker (MockerFixture): Pytest-mock fixture for creating mock objects.
            db_session (Session): SQLAlchemy session fixture.

        Returns:
            UserRepositoryInterface: A mocked instance of the UserRepository.
        """
        user_repository = mocker.Mock(spec=UserRepository(db_session))
        return user_repository

    @pytest.fixture
    def get_user_use_case(
        self, user_repository: UserRepositoryInterface, mocker: MockerFixture
    ) -> CreateUserUseCaseInterface:
        """
        Fixture that sets up the GetUserUseCase with a mocked UserRepository.

        Args:
            user_repository (UserRepositoryInterface): The UserRepository fixture.

        Returns:
            GetUserUseCaseInterface: An instance of GetUserUseCase with the mock UserRepository.
        """
        get_user_use_case = mocker.Mock(GetUserUseCase(user_repository=user_repository))
        return get_user_use_case

    @pytest.fixture
    def get_user_controller(self, get_user_use_case: GetUserUseCaseInterface) -> GetUserController:
        """
        Fixture that creates an instance of GetUserController.

        Args:
            get_user_use_case (GetUserUseCaseInterface): The GetUserUseCase fixture.

        Returns:
            GetUserController: An instance of GetUserController with the given GetUserUseCase.
        """
        get_user_controller = GetUserController(get_user_use_case=get_user_use_case)
        return get_user_controller

    def test_route_returns_user_data_when_email_exists(
        self,
        get_user_controller: GetUserController,
        user_dto: UserDTO,
    ):
        """
        Test that the route method of GetUserController returns user data when the email exists.

        Args:
            get_user_controller (GetUserController): The GetUserController fixture.
            user_dto (UserDTO): The UserDTO fixture.
        """
        http_request = HttpRequest(query={"email": user_dto.email})
        get_user_controller.get_user_use_case.get_user_by_email.return_value = {
            "data": user_dto,
            "success": True,
            "status_code": 200,
        }
        response = get_user_controller.route(http_request=http_request)

        assert response.status_code == 200
        assert response.body == user_dto

    def test_route_when_query_params_is_not_passed(self, get_user_controller: GetUserController):
        """
        Test that the route method of GetUserController returns user data when the email exists.

        Args:
            get_user_controller (GetUserController): The GetUserController fixture.
        """
        http_request = HttpRequest()
        get_user_controller.get_user_use_case.get_user_by_email.return_value = None
        response = get_user_controller.route(http_request=http_request)

        assert response.status_code == HttpErrors.error_400()["status_code"]
        assert response.body == HttpErrors.error_400()["body"]

    def test_route_returns_user_data_when_email_does_not_exists(self, get_user_controller: GetUserController):
        """
        Test that the route method of GetUserController returns user data when the email exists.

        Args:
            get_user_controller (GetUserController): The GetUserController fixture.
        """
        http_request = HttpRequest()
        get_user_controller.get_user_use_case.get_user_by_email.return_value = None
        response = get_user_controller.route(http_request=http_request)

        assert response.status_code == HttpErrors.error_400()["status_code"]
        assert response.body == HttpErrors.error_400()["body"]
