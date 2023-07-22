from enum import Enum


class UserErrorsEnum(Enum):
    """
    Enum class representing common errors related to user operations (CRUD).

    Attributes:
        CREATE_ERROR (str): An error that occurs when creating a user.
        READ_NOT_FOUND (str): An error that occurs when trying to read a user that does not exist.
        UPDATE_ERROR (str): An error that occurs when updating a user.
        DELETE_ERROR (str): An error that occurs when deleting a user.
        NOT_AUTHORIZED (str): An error that occurs when a user is not authorized to perform an operation.
        EMAIL_ALREADY_EXISTS (str): An error that occurs when trying to create a user with an email that already exists.
        DEFAULT_ERROR (str): The default error message for undefined errors. The value is "An undefined error occurred."
    """

    CREATE_ERROR = "Error creating user."
    READ_NOT_FOUND = "User not found."
    UPDATE_ERROR = "Error updating user."
    DELETE_ERROR = "Error deleting user."
    NOT_AUTHORIZED = "User not authorized to perform this operation."
    EMAIL_ALREADY_EXISTS = "A user with this email already exists."
    DEFAULT_ERROR = "An undefined error occurred."
