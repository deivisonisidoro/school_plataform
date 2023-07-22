from sqlalchemy.orm import Session
from dataclasses import dataclass
from src.applications.dtos import UserDTO
from src.infra.db.relational_db.models import UserModel
from src.domain.repositories.user import UserRepositoryInterface


@dataclass
class UserRepository(UserRepositoryInterface):
    """Repository implementation for user data storage using a relational database.

    Attributes:
        db (Session): The SQLAlchemy session for database operations.
    """

    db: Session

    def create_user(self, user: UserDTO) -> UserDTO:
        """Create a new user.

        Args:
            user (UserDTO): The user DTO containing the user data.

        Returns:
            user_dto (UserDTO): The created user DTO.
        """
        db_user = UserModel(name=user.name, email=user.email, password=user.password, created_at=user.created_at)
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        return UserDTO(
            id=db_user.id,
            name=db_user.name,
            email=db_user.email,
            password=db_user.password,
            created_at=db_user.created_at,
        )

    def get_user_by_email(self, email: str) -> UserDTO | None:
        """Retrieve a user by their email from the database.

        Args:
            email (str): The email of the user to retrieve.

        Returns:
            user_dto (UserDTO): The user DTO if found, or None if the user is not found.
        """
        db_user = self.db.query(UserModel).filter_by(email=email).first()
        if db_user:
            return UserDTO(
                id=db_user.id,
                name=db_user.name,
                email=db_user.email,
                password=db_user.password,
                created_at=db_user.created_at,
            )
