from pytest_mock import MockerFixture

from src.applications.dtos.user import UserDTO
from src.applications.use_cases.user.create_user import CreateUserUseCase
from src.applications.enums.user.errors import UserErrorsEnum
from src.infra.db.settings.connection import DBConnectionHandler
from src.infra.repositories.user import UserRepository


class TestCreateUserUseCase:
    """Test suite for the CreateUserUseCase class."""

    def test_create_user_correctly(self, mocker: MockerFixture, db_connection: DBConnectionHandler):
        """
        Test the create_user method of CreateUserUseCase when a user is created correctly.

        This test ensures that the create_user method of CreateUserUseCase correctly handles the creation
        of a new user by verifying that the expected user DTO is returned and that the create_user method
        of the user repository is called with the correct arguments.

        Args:
            mocker (MockerFixture): The pytest mocker fixture.
            db_connection (DBConnectionHandler): A database connection handler for the test database.

        """
        user_repository = mocker.Mock(spec=UserRepository(db_connection=db_connection))
        user_service = CreateUserUseCase(user_repository=user_repository)

        user_dto = UserDTO(
            id=None,
            name="John Doe",
            email="johndoe@example.com",
            password="password123",
            created_at=None,
        )
        created_user_dto = UserDTO(
            name="John Doe",
            email="johndoe@example.com",
            password="password123",
            id=None,
            created_at=None,
        )

        user_repository.create_user.return_value = created_user_dto
        user_repository.get_user_by_email.return_value = None
        result = user_service.create_user(user_dto)
        assert {"data": result, "success": True}
        user_repository.create_user.assert_called_once_with(user_dto)

    def test_create_user_when_the_user_has_already_been_created(
        self, mocker: MockerFixture, db_connection: DBConnectionHandler
    ):
        """
        Test the create_user method of CreateUserUseCase when the user has already been created.

        This test verifies that the create_user method of CreateUserUseCase correctly handles the case
        when a user with the same email already exists by ensuring that the appropriate error response is returned.

        Args:
            mocker (MockerFixture): The pytest mocker fixture.
            db_connection (DBConnectionHandler): A database connection handler for the test database.

        """
        user_repository = mocker.Mock(spec=UserRepository(db_connection=db_connection))
        user_service = CreateUserUseCase(user_repository=user_repository)

        user_dto = UserDTO(
            id=None, name="John Doe", email="johndoe@example.com", password="password123", created_at=None
        )
        created_user_dto = UserDTO(
            name="John Doe", email="johndoe@example.com", password="password123", id=None, created_at=None
        )

        user_repository.create_user.return_value = created_user_dto
        user_repository.get_user_by_email.return_value = created_user_dto
        result = user_service.create_user(user_dto)

        assert result == {"data": UserErrorsEnum.EMAIL_ALREADY_EXISTS.value, "success": False}
