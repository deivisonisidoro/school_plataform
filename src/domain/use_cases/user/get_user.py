from abc import ABC, abstractmethod
from dataclasses import dataclass
from src.applications.dtos.user import UserDTO
from src.domain.enums.user.errors import UserErrorsEnum
from src.domain.repositories.user import UserRepositoryInterface


@dataclass
class GetUserUseCaseInterface(ABC):
    """
    Abstract class representing the use case for getting a user by email.

    This class defines the contract for the use case responsible for retrieving
    a user from the data source using their email.

    Attributes:
        user_repository (UserRepositoryInterface): The repository that provides
            access to the user data.
        user_dto (UserDTO): The user DTO class used to transfer user data between
            layers of the application.
        user_errors_enum (UserErrorsEnum): Enum class representing common errors related
            to user operations (CRUD).

    """

    user_repository: UserRepositoryInterface
    user_dto: UserDTO = UserDTO
    user_errors_enum = UserErrorsEnum

    @abstractmethod
    def get_user_by_email(self, email: str) -> dict:
        """
        Abstract method to retrieve a user by their email.

        This method should be implemented by the subclasses to fetch a user's
        data from the data source based on their email.

        Args:
            email (str): The email of the user to retrieve.

        Returns:
            details (dict): A dictionary containing user details, such as user_id, name,
                and email, retrieved from the data source. If the user is not found,
                it may return an error dictionary using the user_errors_enum.

        Raises:
            ValueError: If the email parameter is empty or invalid.
            Any other specific exceptions: If there are errors related to data access,
                connectivity, or other issues while retrieving the user.

        """
