import pytest
from pytest_mock import MockerFixture
from sqlalchemy.orm import Session

from src.applications.dtos.user import UserDTO
from src.applications.use_cases.user.get_user_by_email import GetUserUseCase
from src.domain.enums.user_error import UserErrorsEnum
from src.domain.repositories.user import UserRepositoryInterface
from src.domain.use_cases.user.get_user import GetUserUseCaseInterface
from src.infra.repositories.user import UserRepository


class TestGetUserByEmail:
    """
    Test cases for the GetUserUseCase class.
    """

    @pytest.fixture
    def user_dto(self) -> UserDTO:
        """
        Fixture that returns a sample UserDTO instance for testing.

        Returns:
            user_dto (UserDTO): A UserDTO instance representing a sample user.
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
            user_repository (UserRepositoryInterface): A mocked instance of the UserRepository.
        """
        user_repository = mocker.Mock(spec=UserRepository(db_session))
        return user_repository

    @pytest.fixture
    def get_user_use_case(self, user_repository: UserRepositoryInterface) -> GetUserUseCaseInterface:
        """
        Fixture that sets up the GetUserUseCase with a mocked UserRepository.

        Args:
            user_repository (UserRepositoryInterface): The UserRepository fixture.

        Returns:
            get_user_use_case (GetUserUseCaseInterface): An instance of GetUserUseCase with the mock UserRepository.
        """
        get_user_use_case = GetUserUseCase(user_repository=user_repository)
        return get_user_use_case

    def test_get_user_by_email_when_return_a_user(
        self,
        get_user_use_case: GetUserUseCaseInterface,
        user_dto: UserDTO,
        user_repository: UserRepositoryInterface,
    ) -> None:
        """
        Test the get_user_by_email method of GetUserUseCase to ensure it returns the correct user data.

        Args:
            get_user_use_case (GetUserUseCaseInterface): The GetUserUseCase fixture.
            user_dto (UserDTO): UserDTO fixture containing sample user data.
            user_repository (UserRepositoryInterface): An instance of UserRepository.

        """
        user_repository.get_user_by_email.return_value = user_dto
        result = get_user_use_case.get_user_by_email(email="johndoe@example.com")
        assert result["data"] == user_dto

    def test_get_user_by_email_when_not_found_a_user(
        self,
        get_user_use_case: GetUserUseCaseInterface,
        user_repository: UserRepositoryInterface,
    ) -> None:
        """
        Test the get_user_by_email method of GetUserUseCase when a user is not found.

        Args:
            get_user_use_case (GetUserUseCaseInterface): The GetUserUseCase fixture.
            user_repository (UserRepositoryInterface): The UserRepository fixture.

        """
        user_repository.get_user_by_email.return_value = None
        result = get_user_use_case.get_user_by_email(email="test@example.com")
        assert result["data"] == UserErrorsEnum.READ_NOT_FOUND.value

    def test_get_user_by_email_when_return_unknown_error(
        self,
        get_user_use_case: GetUserUseCaseInterface,
    ) -> None:
        """
        Test the get_user_by_email method of GetUserUseCase when an unknown error occurs.

        Args:
            get_user_use_case (GetUserUseCaseInterface): The GetUserUseCase fixture.

        """
        get_user_use_case.user_repository.get_user_by_email.side_effect = Exception("Unknown error")
        result = get_user_use_case.get_user_by_email(email="test@example.com")
        assert result["data"] == UserErrorsEnum.DEFAULT_ERROR.value
