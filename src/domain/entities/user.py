from datetime import datetime
from typing import Optional
from dataclasses import dataclass


@dataclass
class UserEntity:
    """Class representing a user.

    Attributes:
        id (Optional[int]): The user's ID.
        name (str): The user's name.
        email (str): The user's email address.
        password (str): The user's password.
        created_at (datetime): The timestamp when the user was created.
    """

    id: Optional[int]
    name: str
    email: str
    password: str
    created_at: Optional[datetime]

    def __str__(self):
        """Return a string representation of the user.

        Returns:
            (str): A string representation of the user.
        """
        return f"User(id={self.id}, name={self.name}, email={self.email})"
