from abc import ABC, abstractmethod
from dataclasses import dataclass

from src.applications.dtos.user import UserDTO
from src.domain.enums.user.errors import UserErrorsEnum
from src.domain.enums.user.success import UserSuccessEnum
from src.domain.repositories.user import UserRepositoryInterface
from src.domain.entities.user import UserEntity


@dataclass
class DeleteUserUseCaseInterface(ABC):
    """
    Interface for the DeleteUser use case.

    This interface defines the contract for the DeleteUser use case and enforces the implementation of
    the Delete_user method.

    Attributes:
        user_repository (UserRepositoryInterface): The user repository interface.
        user_entity (UserEntity): The user entity class.
        user_dto (UserDTO): The user DTO class.
    """

    user_repository: UserRepositoryInterface
    user_entity: UserEntity = UserEntity
    user_dto: UserDTO = UserDTO
    user_errors_enum = UserErrorsEnum
    user_success_enum = UserSuccessEnum

    @abstractmethod
    def delete_user(self, user_id: int) -> dict:
        """
        Delete a user by their ID.

        Args:
            user_id (int): The ID of the user to delete.

        Returns:
            dict: A dictionary indicating the success or failure of the deletion operation.

        Raises:
            NotImplementedError: If the method is not implemented by a concrete subclass.
            Exception: If an error occurs while deleting the user.
        """
