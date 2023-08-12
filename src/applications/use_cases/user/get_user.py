from dataclasses import dataclass

from src.applications.dtos.user import UserDTO
from src.domain.enums.user.errors import UserErrorsEnum
from src.domain.repositories.user import UserRepositoryInterface
from src.domain.use_cases.user.get_user import GetUserUseCaseInterface


@dataclass
class GetUserUseCase(GetUserUseCaseInterface):
    """
    Concrete implementation of the GetUserUseCaseInterface.

    This use case retrieves a user from the data source using their email.

    Attributes:
        user_repository (UserRepositoryInterface): The repository that provides
            access to the user data.
        user_dto (UserDTO): The user DTO class used to transfer user data between
            layers of the application.
        user_errors_enum (UserErrorsEnum): Enum class representing common errors related
            to user operations (CRUD).

    Methods:
        get_user(email: str) -> dict:
            Retrieves a user by their email from the data source.

    """

    user_repository: UserRepositoryInterface
    user_dto: UserDTO = UserDTO
    user_errors_enum = UserErrorsEnum

    def get_user_by_email(self, email: str) -> dict:
        """
        Retrieves a user by their email from the data source.

        Args:
            email (str): The email of the user to retrieve.

        Returns:
            dict: A dictionary containing the user details if found. If the user is not found,
                it returns a dictionary with error details using the user_errors_enum.
        """
        user_dto = self.user_repository.get_user_by_email(email=email)
        if user_dto is None:
            return {"data": self.user_errors_enum.READ_NOT_FOUND.value, "success": False}
        user_entity = user_dto.to_domain()
        dto = user_dto.to_dto(user_entity)
        return {"data": dto, "success": True}
