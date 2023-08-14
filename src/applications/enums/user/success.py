from enum import Enum


class UserSuccessEnum(Enum):
    """
    Enum class representing success states related to user operations (CRUD).

    Attributes:
        CREATE_SUCCESS (str): Successful user creation message.
        UPDATE_SUCCESS (str): Successful user update message.
        DELETE_SUCCESS (str): Successful user deletion message.
        READ_SUCCESS (str): Successful user retrieval message.
    """

    CREATE_SUCCESS = "User created successfully."
    UPDATE_SUCCESS = "User updated successfully."
    DELETE_SUCCESS = "User deleted successfully."
    READ_SUCCESS = "User retrieved successfully."
