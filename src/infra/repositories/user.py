from typing import Optional
from src.applications.dtos import UserDTO
from src.infra.db.settings.connection import DBConnectionHandler
from src.infra.models import UserModel
from src.domain.repositories.user import UserRepositoryInterface


class UserRepository(UserRepositoryInterface):
    """
    Repository implementation for user data storage using a relational database.

    This repository provides methods for creating and retrieving user data from the database.
    """

    def __init__(self, db_connection: DBConnectionHandler):
        self.db_connection = db_connection

    def create_user(self, user: UserDTO) -> UserDTO:
        """
        Create a new user.

        Args:
            user (UserDTO): The user DTO containing the user data.

        Returns:
            user_dto (UserDTO): The created user DTO.

        Raises:
            Exception: If an error occurs during user creation.
        """
        with self.db_connection as db_connection:
            try:
                db_user = UserModel(
                    name=user.name, email=user.email, password=user.password, created_at=user.created_at
                )
                db_connection.session.add(db_user)
                db_connection.session.commit()
                db_connection.session.refresh(db_user)
                return UserDTO(
                    id=db_user.id,
                    name=db_user.name,
                    email=db_user.email,
                    password=db_user.password,
                    created_at=db_user.created_at,
                )
            except Exception as exception:
                db_connection.session.rollback()
                raise exception
            finally:
                db_connection.session.close()

    def get_user_by_email(self, email: str) -> Optional[UserDTO]:
        """
        Retrieve a user by their email from the database.

        Args:
            email (str): The email of the user to retrieve.

        Returns:
            UserDTO | None: The user DTO if found, or None if the user is not found.

        Raises:
            Exception: If an error occurs while retrieving the user.
        """
        with self.db_connection as db_connection:
            try:
                db_user = db_connection.session.query(UserModel).filter_by(email=email).first()
                if db_user:
                    return UserDTO(
                        id=db_user.id,
                        name=db_user.name,
                        email=db_user.email,
                        password=db_user.password,
                        created_at=db_user.created_at,
                    )
                return None
            except Exception as exception:
                db_connection.session.rollback()
                raise exception
            finally:
                db_connection.session.close()
