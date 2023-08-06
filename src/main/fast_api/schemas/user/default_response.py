from pydantic import BaseModel

from src.main.fast_api.schemas.user.user_out import UserOut


class DefaultResponse(BaseModel):
    """
    Pydantic model representing the default dictionary response.

    This model is used to structure the response data with `detail` and `status_code` fields.
    The `detail` field can accept any data type (str, int, float, bool, or custom types),
    making it flexible to handle various types of responses.

    Attributes:
        detail (Union[UserOut, str]): The data representing the response details, which can be of any data type (str, int, float, bool, or custom types).
        status_code (int): The HTTP status code representing the response status.

    """

    type: str
    attributes: UserOut

    class ConfigDict:
        """
        Pydantic configuration for the User schema.

        The Config class allows configuring additional settings for the Pydantic model.

        Attributes:
            from_attributes (bool): If set to True, Pydantic will allow the model to work with SQLAlchemy's ORM,
                             enabling automatic conversion between SQLAlchemy models and Pydantic models.

        """

        from_attributes = True
