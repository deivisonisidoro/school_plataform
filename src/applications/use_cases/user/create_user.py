from dataclasses import dataclass

from src.applications.dtos.user import UserDTO
from src.applications.enums.user.errors import UserErrorsEnum
from src.domain.repositories.user import UserRepositoryInterface
from src.domain.use_cases.user.create_user import CreateUserUseCaseInterface
from src.domain.entities.user import UserEntity


@dataclass
class CreateUserUseCase(CreateUserUseCaseInterface):
    """
    Create user use case.

    This class implements the CreateUserUseCaseInterface and provides the functionality to create a new user.

    Attributes:
        user_repository (UserRepositoryInterface): The user repository interface.
        user_entity (UserEntity): The user entity class.
        user_dto (UserDTO): The user DTO class.

    Methods:
        create_user(user_dto: UserDTO) -> UserDTO:
            Create a new user with the provided user DTO.

    """

    user_repository: UserRepositoryInterface
    user_dto = UserDTO
    user_entity = UserEntity
    user_errors_enum = UserErrorsEnum

    def create_user(self, user_dto: UserDTO) -> UserDTO:
        """
        Create a new user with the provided user DTO.

        Args:
            user_dto (UserDTO): The user DTO containing the user data.

        Returns:
            user_dto (UserDTO): The created user DTO.
        """
        user_entity = user_dto.to_domain()
        dto = user_dto.to_dto(user_entity)
        user = self.user_repository.get_user_by_email(email=dto.email)
        if user:
            return {"data": self.user_errors_enum.EMAIL_ALREADY_EXISTS.value, "success": False}
        user_created = self.user_repository.create_user(dto)
        return {"data": user_created, "success": True}
