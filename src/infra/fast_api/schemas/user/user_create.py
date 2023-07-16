from src.infra.fast_api.schemas.user.user_base import UserBase


class UserCreate(UserBase):
    """
    Schema for creating a new user.

    This schema inherits from UserBase and adds the password field for creating a new user.

    Attributes:
        password (str): The user's password.

    """

    password: str
