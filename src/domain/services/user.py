from abc import ABC, abstractmethod
from pydantic.dataclasses import dataclass

from applications.dtos.user import UserDTO
from domain.repositories.user import UserRepositoryInterface
from src.domain.entities.user import UserEntity


@dataclass
class UserServiceInterface(ABC):
    """
    Interface for user services.

    This interface defines the contract for user services and enforces the implementation of all methods.

    Attributes:
        user_repository (UserRepositoryInterface): The user repository interface.
        user_entity (UserEntity): The user entity class.
        user_dto (UserDTO): The user DTO class.

    """

    user_repository: UserRepositoryInterface
    user_entity: UserEntity = UserEntity
    user_dto: UserDTO = UserDTO

    @abstractmethod
    def create_user(self, user_dto: UserDTO) -> UserDTO:
        """
        Create a new user.

        Args:
            user_dto (UserDTO): The user DTO containing the user data.

        Returns:
            UserDTO: The created user DTO.
        """
