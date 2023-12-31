from abc import ABC, abstractmethod
from typing import Optional
from src.applications.dtos import UserDTO


class UserRepositoryInterface(ABC):
    """
    Interface for user repository.

    This interface defines methods for creating, retrieving, and deleting user data from the repository.

    """

    @abstractmethod
    def create_user(self, user: UserDTO) -> UserDTO:
        """
        Create a new user.

        Args:
            user (UserDTO): The user DTO containing the user data.

        Returns:
            UserDTO: The created user DTO.

        Raises:
            NotImplementedError: If the method is not implemented by a concrete subclass.
            Exception: If an error occurs during user creation.
        """

    @abstractmethod
    def get_user_by_email(self, email: str) -> Optional[UserDTO]:
        """
        Get a user by their email.

        This method should be implemented by the concrete subclasses to retrieve
        a user DTO from the data source based on their email.

        Args:
            email (str): The email of the user to retrieve.

        Returns:
            UserDTO | None: The user DTO representing the user's information if found, or None if not found.

        Raises:
            NotImplementedError: If the method is not implemented by a concrete subclass.
            Exception: If an error occurs while retrieving the user.
        """

    @abstractmethod
    def get_user_by_id(self, user_id: int) -> Optional[UserDTO]:
        """
        Get a user by their ID.

        This method should be implemented by the concrete subclasses to retrieve
        a user DTO from the data source based on their ID.

        Args:
            user_id (int): The ID of the user to retrieve.

        Returns:
            UserDTO | None: The user DTO representing the user's information if found, or None if not found.

        Raises:
            NotImplementedError: If the method is not implemented by a concrete subclass.
            Exception: If an error occurs while retrieving the user.
        """

    @abstractmethod
    def delete_user(self, user_id: int) -> None:
        """
        Delete a user by their ID.

        Args:
            user_id (int): The ID of the user to delete.

        Raises:
            NotImplementedError: If the method is not implemented by a concrete subclass.
            Exception: If an error occurs while deleting the user.
        """
