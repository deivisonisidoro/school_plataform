from enum import Enum


class UserErrorsEnum(Enum):
    """
    Enum class representing common errors related to user operations (CRUD).

    Attributes:
        CREATE_ERROR (dict): An error that occurs when creating a user.
        READ_NOT_FOUND (dict): An error that occurs when trying to read a user that does not exist.
        UPDATE_ERROR (dict): An error that occurs when updating a user.
        DEFAULT_ERROR (str): The default error message for undefined errors. The value is "An undefined error occurred."
    """

    CREATE_ERROR = "Error creating user."
    READ_NOT_FOUND = "User not found."
    UPDATE_ERROR = "Error updating user."
    DELETE_ERROR = "Error deleting user."
    DEFAULT_ERROR = "An undefined error occurred."
