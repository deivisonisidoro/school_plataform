from abc import ABC, abstractmethod
from dataclasses import dataclass
from sqlalchemy.orm import Session

from src.applications.dtos import UserDTO


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

    @abstractmethod
    def get_user_by_email(self, email: str) -> UserDTO:
        """Get a user by their email.

        This method should be implemented by the concrete subclasses to retrieve
        a user entity from the data source based on their email.

        Args:
            email (str): The email of the user to retrieve.

        Returns:
            user_dto (UserDTO): The user DTO representing the user's information.
        """
