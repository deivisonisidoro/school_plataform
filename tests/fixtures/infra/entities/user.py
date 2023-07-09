from datetime import datetime
import pytest
from src.domain.entities.user import UserEntity


@pytest.fixture
def user_entity():
    """Fixture for creating a UserEntity instance.

    Returns:
        UserEntity: A UserEntity instance with predefined attributes.
    """
    return UserEntity(id=1, name="john", email="john@example.com", password="password", created_at=datetime.now())
