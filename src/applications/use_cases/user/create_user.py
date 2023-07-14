from dataclasses import dataclass

from src.applications.dtos.user import UserDTO
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
    user_entity: UserEntity = UserEntity
    user_dto: UserDTO = UserDTO

    def create_user(self, user_dto: UserDTO) -> UserDTO:
        """
        Create a new user with the provided user DTO.

        Args:
            user_dto (UserDTO): The user DTO containing the user data.

        Returns:
            UserDTO: The created user DTO.

        """
        user_entity = self.user_entity(
            id=user_dto.id,
            name=user_dto.name,
            email=user_dto.email,
            password=user_dto.password,
            created_at=user_dto.created_at,
        )
        user_dto = self.user_dto(
            id=user_entity.id,
            name=user_entity.name,
            email=user_entity.email,
            password=user_entity.password,
            created_at=user_entity.created_at,
        )
        return self.user_repository.create_user(user_dto)
