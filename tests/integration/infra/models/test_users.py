import pytest
from sqlalchemy.exc import IntegrityError

from src.infra.db.settings.connection import DBConnectionHandler

from src.infra.models import UserModel


class TestUserModel:
    """Test cases for the UserModel class."""

    def test_create_user(self, db_connection: DBConnectionHandler):
        """Test creating a user and retrieving it from the database.

        Args:
            db_connection (DBConnectionHandler): A database connection handler for the test database.
        """
        with db_connection as db:
            user = UserModel(name="John Doe", email="john@example.com", password="password")
            db.session.add(user)
            db.session.commit()

            fetched_user = db.session.query(UserModel).filter_by(email="john@example.com").first()

            assert fetched_user.name == "John Doe"
            assert fetched_user.email == "john@example.com"
            assert fetched_user.password == "password"

    def test_unique_email_constraint(self, db_connection: DBConnectionHandler):
        """Test the unique email constraint by attempting to create two users with the same email.

        Args:
            db_connection (DBConnectionHandler): A database connection handler for the test database.

        """

        user1 = UserModel(name="John Doe", email="john@example.com", password="password1")
        user2 = UserModel(name="Jane Smith", email="john@example.com", password="password2")
        with db_connection as db:
            db.session.add(user1)

            with pytest.raises(IntegrityError):
                db.session.add(user2)
                db.session.commit()

            db.session.rollback()

            fetched_user = db.session.query(UserModel).filter_by(email="john@example.com").first()
            assert fetched_user is None
