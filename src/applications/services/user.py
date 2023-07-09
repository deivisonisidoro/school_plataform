from pydantic.dataclasses import dataclass

from applications.dtos.user import UserDTO
from domain.repositories.user import UserRepositoryInterface
from domain.services.user import UserServiceInterface
from src.domain.entities.user import UserEntity


@dataclass
class UserService(UserServiceInterface):
    """
    Service for managing user operations.

    Attributes:
        user_repository (UserRepositoryInterface): The user repository for database operations.
        user_entity (UserEntity): The user entity class.
        user_dto (UserDTO): The user DTO class.
    """

    user_repository: UserRepositoryInterface
    user_entity: UserEntity = UserEntity
    user_dto: UserDTO = UserDTO

    def create_user(self, user_dto: UserDTO) -> UserDTO:
        """
        Create a new user.

        Args:
            user_dto (UserDTO): The user DTO containing the user data.

        Returns:
            user_dto (UserDTO): The created user DTO.
        """

        user_entity = self.user_entity(**user_dto)
        user_dto = self.user_dto(**user_entity)
        return self.user_repository.create_user(user_dto)
