from dataclasses import dataclass

from src.applications.dtos.user import UserDTO
from src.domain.enums.user_error import UserErrorsEnum
from src.domain.repositories.user import UserRepositoryInterface
from src.domain.use_cases.user.get_user_by_email import GetUserByEmailUseCaseInterface


@dataclass
class GetUserByEmailUseCase(GetUserByEmailUseCaseInterface):
    """
    Concrete implementation of the GetUserByEmailUseCaseInterface.

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

    def get_user(self, email: str) -> dict:
        """
        Retrieves a user by their email from the data source.

        Args:
            email (str): The email of the user to retrieve.

        Returns:
            dict: A dictionary containing the user details if found. If the user is not found,
                it returns a dictionary with error details using the user_errors_enum.

        Raises:
            : If there are errors related to data access, connectivity,
                or other issues while retrieving the user.

        """
        try:
            user = self.user_repository.get_user_by_email(email=email)
            if not user:
                return {"detail": self.user_errors_enum.READ_NOT_FOUND.value, "status_code": 404}
            return {"detail": user, "status_code": 200}
        except Exception:
            return {"detail": self.user_errors_enum.DEFAULT_ERROR.value, "status_code": 500}
