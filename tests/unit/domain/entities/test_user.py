import pytest
from src.domain.entities.user import UserEntity
from datetime import datetime


@pytest.fixture
def user():
    """Fixture for creating a UserEntity instance.

    Returns:
        UserEntity: A UserEntity instance with predefined attributes.
    """
    return UserEntity(
        id=1,
        name="john",
        email="john@example.com",
        password="password",
        created_at=datetime.now()
    )


class TestUserEntity:
    """Test class for UserEntity.

    The TestUserEntity class contains test methods to verify the behavior of the UserEntity class.
    """

    def test_user_str_representation(self, user):
        """Test the string representation of UserEntity.

        Args:
            user (UserEntity): The UserEntity instance to test.

        The test verifies that the string representation of UserEntity matches the expected format.
        """
        expected_str = "User(id=1, name=john, email=john@example.com)"
        assert str(user) == expected_str

    def test_user_attributes(self, user):
        """Test the attributes of UserEntity.

        Args:
            user (UserEntity): The UserEntity instance to test.

        The test verifies that the UserEntity instance has the expected attribute values.
        """
        assert user.id == 1
        assert user.name == "john"
        assert user.email == "john@example.com"
        assert user.password == "password"
        assert isinstance(user.created_at, datetime)

    def test_user_optional_id(self):
        """Test the optional ID attribute of UserEntity.

        The test creates a UserEntity instance with a None value for the ID attribute and verifies that
        the ID attribute is set to None.
        """
        user = UserEntity(
            id=None,
            name="john",
            email="john@example.com",
            password="password",
            created_at=datetime.now()
        )
        assert user.id is None
