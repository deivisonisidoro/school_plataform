from abc import ABC, abstractmethod
from dataclasses import dataclass

from src.applications.dtos.user import UserDTO
from src.domain.repositories.user import UserRepositoryInterface
from src.domain.entities.user import UserEntity


@dataclass
class CreateUserUseCaseInterface(ABC):
    """
    Interface for the CreateUser use case.

    This interface defines the contract for the CreateUser use case and enforces the implementation of
    the create_user method.

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
