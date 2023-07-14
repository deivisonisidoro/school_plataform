from sqlalchemy.orm import Session
from dataclasses import dataclass

from src.applications.dtos import UserDTO
from src.infra.db.models import UserModel
from src.domain.repositories.user import UserRepositoryInterface


@dataclass
class UserRepository(UserRepositoryInterface):
    """Repository implementation for user data storage using a relational database.

    Attributes:
        db (Session): The SQLAlchemy session for database operations.
    """

    db: Session

    def create_user(self, user: UserDTO) -> UserDTO:
        """Create a new user.

        Args:
            user (UserDTO): The user DTO containing the user data.

        Returns:
            user_dto (UserDTO): The created user DTO.
        """
        user_data = UserModel(
            name=user.name,
            email=user.email,
            password=user.password,
            created_at=user.created_at,
        )
        self.db.add(user_data)
        self.db.commit()
        self.db.refresh(user_data)
        return UserDTO(
            id=user_data.id,
            name=user_data.name,
            email=user_data.email,
            password=user_data.password,
            created_at=user_data.created_at,
        )
