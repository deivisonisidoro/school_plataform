from datetime import datetime
from pydantic import BaseModel


class UserBase(BaseModel):
    """
    Base schema for user data.

    This schema defines the common fields for creating and updating a user.

    Attributes:
        name (str): The name of the user, with a maximum length of 50 characters.
        email (str): The email address of the user, with a maximum length of 255 characters.

    """

    name: str
    email: str


class User(UserBase):
    """
    Schema for user data.

    This schema inherits from UserBase and adds the id and created_at fields representing user details.

    Attributes:
        id (int): The primary key of the user table.
        created_at (datetime): The timestamp for when the user was created.

    """

    id: int
    created_at: datetime

    class Config:
        """
        Pydantic configuration for the User schema.

        The Config class allows configuring additional settings for the Pydantic model.

        Attributes:
            from_attributes (bool): If set to True, Pydantic will allow the model to work with SQLAlchemy's ORM,
                             enabling automatic conversion between SQLAlchemy models and Pydantic models.

        """

        from_attributes = True
