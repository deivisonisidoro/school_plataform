from src.applications.dtos.user import UserDTO
from datetime import datetime


class TestUserDTO:
    """Class for testing the UserDTO class."""

    def test_user_dto_creation(self):
        """Test the creation of a UserDTO object.

        This test verifies if a UserDTO object is created correctly with the provided arguments.

        It checks if the attributes of the UserDTO object match the expected values.
        """
        user = UserDTO(
            id=1, name="John Doe", email="johndoe@example.com", password="password", created_at=datetime.now()
        )

        assert user.id == 1
        assert user.name == "John Doe"
        assert user.email == "johndoe@example.com"
        assert user.password == "password"
        assert user.created_at is not None

    def test_user_dto_creation_with_optional_fields(self):
        """Test the creation of a UserDTO object with optional fields.

        This test verifies if a UserDTO object is created correctly when optional fields are not provided.

        It checks if the optional fields are set to None.

        """
        user = UserDTO(id=None, name="Jane Smith", email="janesmith@example.com", password="password", created_at=None)

        assert user.id is None
        assert user.name == "Jane Smith"
        assert user.email == "janesmith@example.com"
        assert user.password == "password"
        assert user.created_at is None
