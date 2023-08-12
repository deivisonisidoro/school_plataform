import pytest

from src.applications.dtos import UserDTO
from src.infra.db.settings.connection import DBConnectionHandler
from src.infra.repositories.user import UserRepository
from src.domain.repositories.user import UserRepositoryInterface


class TestUserRepository:
    """Test cases for the UserRepository class."""

    @pytest.fixture
    def user_repository(self, db_connection: DBConnectionHandler) -> UserRepositoryInterface:
        """Create an instance of UserRepository with a test database session.

        Args:
            db_connection (DBConnectionHandler): A database connection handler for the test database.

        Returns:
            user_repository = UserRepositoryInterface: An instance of UserRepository.
        """
        user_repository = UserRepository(db_connection=db_connection)
        return user_repository

    @pytest.fixture
    def user_dto(self) -> UserDTO:
        """
        Fixture that returns a sample UserDTO instance for testing.

        Returns:
            user_dto (UserDTO): A UserDTO instance representing a sample user.
        """
        user_dto = UserDTO(
            id=None,
            name="John Doe",
            email="johndoe@example.com",
            password="password123",
            created_at=None,
        )
        return user_dto

    def test_create_user(
        self,
        user_repository: UserRepositoryInterface,
        user_dto: UserDTO,
    ) -> None:
        """Test creating a new user.

        Args:
            user_repository (UserRepositoryInterface): An instance of UserRepository.
            user_dto (UserDTO): UserDTO fixture containing sample user data.
        """
        created_user = user_repository.create_user(user_dto)
        assert isinstance(created_user, UserDTO)

    def test_create_user_with_exception(self, user_repository: UserRepositoryInterface, user_dto: UserDTO):
        """Test creating a user with an exception raised during creation."""

        user_dto.email = None
        with pytest.raises(Exception):
            user_repository.create_user(user_dto)

    def test_get_user_by_email_when_found_user(
        self,
        user_repository: UserRepositoryInterface,
        user_dto: UserDTO,
    ):
        """
        Test fetching a user by email using UserRepository when found user.

        Args:
            user_repository (UserRepositoryInterface): The UserRepository fixture.
            user_dto (UserDTO): UserDTO fixture containing sample user data.
        """
        created_user = user_repository.create_user(user_dto)
        fetched_user = user_repository.get_user_by_email(email=created_user.email)
        assert isinstance(fetched_user, UserDTO)

    def test_get_user_by_email_when_not_found_user(
        self,
        user_repository: UserRepositoryInterface,
    ):
        """
        Test fetching a user by email using UserRepository when not found user.

        Args:
            user_repository (UserRepositoryInterface): The UserRepository fixture.
            user_dto (UserDTO): UserDTO fixture containing sample user data.
        """
        fetched_user = user_repository.get_user_by_email(email="test@example.com")

        assert not isinstance(fetched_user, UserDTO)

    def test_delete_user(self, user_repository: UserRepositoryInterface, user_dto: UserDTO):
        """
        Test the deletion of a user.

        This test verifies that the 'delete_user' method effectively removes a user from the database.

        Args:
            user_repository (UserRepositoryInterface): An instance of UserRepository.
            user_dto (UserDTO): A UserDTO instance representing a sample user.
        """
        created_user = user_repository.create_user(user_dto)
        user_repository.delete_user(created_user.id)
        fetched_user = user_repository.get_user_by_id(created_user.id)
        assert fetched_user is None

    def test_delete_user_with_invalid_id(self, user_repository: UserRepositoryInterface):
        """
        Test deleting a user with an invalid ID.

        This test verifies that the 'delete_user' method properly handles the scenario where
        an attempt is made to delete a user using an ID that does not exist in the database.

        Args:
            user_repository (UserRepositoryInterface): An instance of UserRepository.

        Raises:
            Exception: If the 'delete_user' method does not handle the invalid ID case correctly.
        """
        with pytest.raises(Exception):
            user_repository.delete_user(9999)
