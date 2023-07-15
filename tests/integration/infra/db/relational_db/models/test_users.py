import pytest
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from src.infra.db.relational_db.models import UserModel


class TestUserModel:
    """Test cases for the UserModel class."""

    def test_create_user(self, db_session: Session):
        """Test creating a user and retrieving it from the database.

        Args:
            db_session (Session): The test database session.

        Returns:
            None
        """
        # Create a user
        user = UserModel(name="John Doe", email="john@example.com", password="password")
        db_session.add(user)
        db_session.commit()

        fetched_user = db_session.query(UserModel).filter_by(email="john@example.com").first()

        assert fetched_user.name == "John Doe"
        assert fetched_user.email == "john@example.com"
        assert fetched_user.password == "password"

    def test_unique_email_constraint(self, db_session: Session):
        """Test the unique email constraint by attempting to create two users with the same email.

        Args:
            db_session (Session): The test database session.

        """

        user1 = UserModel(name="John Doe", email="john@example.com", password="password1")
        user2 = UserModel(name="Jane Smith", email="john@example.com", password="password2")

        db_session.add(user1)

        with pytest.raises(IntegrityError):
            db_session.add(user2)
            db_session.commit()

        db_session.rollback()

        fetched_user = db_session.query(UserModel).filter_by(email="john@example.com").first()
        assert fetched_user is None
