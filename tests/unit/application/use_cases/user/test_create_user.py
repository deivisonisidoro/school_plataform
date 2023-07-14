from pytest_mock import MockerFixture

from src.applications.dtos.user import UserDTO
from src.domain.repositories.user import UserRepositoryInterface
from src.applications.use_cases.user.create_user import CreateUserUseCase


class TestCreateUserUseCase:
    """Test suite for the CreateUserUseCase class."""

    def test_create_user_correctly(self, mocker: MockerFixture):
        """
        Test the create_user method of CreateUserUseCase when a user is created correctly.

        This test ensures that the create_user method of CreateUserUseCase correctly handles the creation
        of a new user by verifying that the expected user DTO is returned and that the create_user method
        of the user repository is called with the correct arguments.

        Args:
            mocker (MockerFixture): The pytest mocker fixture.

        """
        user_repository = mocker.Mock(spec=UserRepositoryInterface)
        user_service = CreateUserUseCase(user_repository=user_repository)

        user_dto = UserDTO(
            id=None, name="John Doe", email="johndoe@example.com", password="password123", created_at=None
        )
        created_user_dto = UserDTO(
            name="John Doe", email="johndoe@example.com", password="password123", id=None, created_at=None
        )

        user_repository.create_user.return_value = created_user_dto

        result = user_service.create_user(user_dto)

        assert result == created_user_dto
        user_repository.create_user.assert_called_once_with(user_dto)
