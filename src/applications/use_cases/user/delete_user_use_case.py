from dataclasses import dataclass

from src.applications.dtos.user import UserDTO
from src.domain.enums.user.errors import UserErrorsEnum
from src.domain.enums.user.success import UserSuccessEnum
from src.domain.repositories.user import UserRepositoryInterface
from src.domain.use_cases.user.delete_user import DeleteUserUseCaseInterface
from src.domain.entities.user import UserEntity


@dataclass
class DeleteUserUseCase(DeleteUserUseCaseInterface):
    """
    Delete user use case.

    This class implements the DeleteUserUseCaseInterface and provides the functionality to Delete a new user.

    Attributes:
        user_repository (UserRepositoryInterface): The user repository interface.
        user_entity (UserEntity): The user entity class.
        user_dto (UserDTO): The user DTO class.

    Methods:
        Delete_user(user_dto: UserDTO) -> UserDTO:
            Delete a new user with the provided user DTO.

    """

    user_repository: UserRepositoryInterface
    user_dto = UserDTO
    user_entity = UserEntity
    user_errors_enum = UserErrorsEnum
    user_success_enum = UserSuccessEnum

    def delete_user(self, user_id: int) -> dict:
        """
        Delete a new user with the provided user DTO.

        Args:
            user_id (int): The ID of the user to delete.

        Returns:
            dict: A dictionary indicating the success or failure of the deletion operation.
        """
        user = self.user_repository.get_user_by_id(user_id=user_id)
        if user is None:
            return {"data": self.user_errors_enum.READ_NOT_FOUND.value, "success": False}
        self.user_repository.delete_user(user_id=user.id)
        return {"data": self.user_success_enum.DELETE_SUCCESS.value, "success": True}
