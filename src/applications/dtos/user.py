from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class UserDTO(BaseModel):
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

    class Config:
        """Configuration for the Pydantic model."""

        orm_mode = True
