import pytest
from datetime import datetime
from sqlalchemy.orm import Session

from src.applications.dtos import UserDTO
from src.infra.db.relational_db.models import UserModel
from src.infra.repositories.user import UserRepository
from src.domain.repositories.user import UserRepositoryInterface


class TestUserRepository:
    """Test cases for the UserRepository class."""

    @pytest.fixture
    def user_repository(self, db_session: Session) -> UserRepositoryInterface:
        """Create an instance of UserRepository with a test database session.

        Args:
            db_session (Session): The test database session.

        Returns:
            UserRepositoryInterface: An instance of UserRepository.
        """
        return UserRepository(db=db_session)

    def test_create_user(self, db_session: Session, user_repository: UserRepositoryInterface) -> None:
        """Test creating a new user.

        Args:
            db_session (Session): The test database session.
            user_repository (UserRepositoryInterface): An instance of UserRepository.

        Returns:
            None
        """

        user_dto = UserDTO(
            id=None,
            name="John Doe",
            email="john@example.com",
            password="password",
            created_at=datetime.now(),
        )

        created_user = user_repository.create_user(user_dto)

        fetched_user = db_session.query(UserModel).filter_by(id=created_user.id).first()

        assert fetched_user.name == "John Doe"
        assert fetched_user.email == "john@example.com"
        assert fetched_user.password == "password"
        assert fetched_user.created_at == user_dto.created_at
