from abc import ABC, abstractmethod
from sqlalchemy.orm import Session
from pydantic.dataclasses import dataclass

from applications.dtos import UserDTO


@dataclass
class UserRepositoryInterface(ABC):
    """Interface for user repository.

    Attributes:
        db (Session): The SQLAlchemy session for database operations.
    """

    db: Session

    @abstractmethod
    def create_user(self, user: UserDTO) -> UserDTO:
        """Create a new user.

        Args:
            user (UserDTO): The user entity to be created.

        Returns:
            user_dto (UserDTO): The created user DTO.
        """
