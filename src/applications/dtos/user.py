from datetime import datetime
from typing import Optional
from dataclasses import dataclass

from src.domain.entities.user import UserEntity


@dataclass
class UserDTO:
    """DTO (Data Transfer Object) for representing a user entity.

    Attributes:
        id (Optional[int]): The user's ID.
        name (str): The user's name.
        email (str): The user's email address.
        password (str): The user's password.
        created_at (Optional[datetime]): The timestamp when the user was created.
    """

    id: Optional[int]
    name: str
    email: str
    password: str
    created_at: Optional[datetime]

    def to_domain(self):
        """Converts the UserDTO to a UserEntity object.

        Returns:
            user_entity (UserEntity): The UserEntity object representing the user.
        """
        user_entity = UserEntity(
            id=self.id,
            name=self.name,
            email=self.email,
            password=self.password,
            created_at=self.created_at,
        )

        return user_entity

    def to_dto(self, user_entity: UserEntity):
        """Converts a UserEntity object to a UserDTO.

        Args:
            user_entity (UserEntity): The UserEntity object to convert.

        Returns:
            user_dto (UserDTO): The UserDTO object representing the user.
        """
        return UserDTO(
            id=user_entity.id,
            name=user_entity.name,
            email=user_entity.email,
            password=user_entity.password,
            created_at=user_entity.created_at,
        )
