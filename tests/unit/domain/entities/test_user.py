from datetime import datetime
from src.domain.entities.user import UserEntity


class TestUserEntity:
    """Test class for UserEntity.

    The TestUserEntity class contains test methods to verify the behavior of the UserEntity class.
    """

    def test_user_str_representation(self, user_entity):
        """Test the string representation of UserEntity.

        Args:
            user_entity (UserEntity): The UserEntity instance to test.

        The test verifies that the string representation of UserEntity matches the expected format.
        """
        expected_str = "User(id=1, name=john, email=john@example.com)"
        assert str(user_entity) == expected_str

    def test_user_attributes(self, user_entity):
        """Test the attributes of UserEntity.

        Args:
            user_entity (UserEntity): The UserEntity instance to test.

        The test verifies that the UserEntity instance has the expected attribute values.
        """
        assert user_entity.id == 1
        assert user_entity.name == "john"
        assert user_entity.email == "john@example.com"
        assert user_entity.password == "password"
        assert isinstance(user_entity.created_at, datetime)

    def test_user_optional_id(self):
        """Test the optional ID attribute of UserEntity.

        The test creates a UserEntity instance with a None value for the ID attribute and verifies that
        the ID attribute is set to None.
        """
        user_entity = UserEntity(
            id=None, name="john", email="john@example.com", password="password", created_at=datetime.now()
        )
        assert user_entity.id is None
