from datetime import datetime

from src.infra.fast_api.schemas.user.user_base import UserBase


class UserOut(UserBase):
    """
    Pydantic schema representing the attributes returned for a user.

    Inherits from UserBase.

    Attributes:
        id (int): The user's ID
        created_at (datetime): The date and time when the user was created
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
