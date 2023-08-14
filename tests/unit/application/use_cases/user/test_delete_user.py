import pytest
from pytest_mock import MockerFixture

from src.applications.dtos.user import UserDTO
from src.applications.use_cases.user.delete_user_use_case import DeleteUserUseCase
from src.applications.enums.user.errors import UserErrorsEnum
from src.applications.enums.user.success import UserSuccessEnum
from src.domain.repositories.user import UserRepositoryInterface
from src.domain.use_cases.user.delete_user import DeleteUserUseCaseInterface
from src.infra.db.settings.connection import DBConnectionHandler
from src.infra.repositories.user import UserRepository


class TestDeleteUserUserCase:
    """
    Test Delete User
    """

    @pytest.fixture
    def user_dto(self) -> UserDTO:
        """
        Fixture that returns a sample UserDTO instance for testing.

        Returns:
        user_dto (UserDTO): A UserDTO instance representing a sample user.
        """
        user_dto = UserDTO(
            id=1,
            name="John Doe",
            email="johndoe@example.com",
            password="password123",
            created_at="2023-07-21 12:34:56",
        )
        return user_dto

    @pytest.fixture
    def user_repository(self, mocker: MockerFixture, db_connection: DBConnectionHandler) -> UserRepositoryInterface:
        """
        Fixture that sets up a mocked UserRepository with a sample user.

        Args:
        mocker (MockerFixture): Pytest-mock fixture for creating mock objects.
        db_connection (DBConnectionHandler): A database connection handler for the test database.

        Returns:
        user_repository (UserRepositoryInterface): A mocked instance of the UserRepository.
        """
        user_repository = mocker.Mock(spec=UserRepository(db_connection=db_connection))
        return user_repository

    @pytest.fixture
    def delete_user_use_case(self, user_repository: UserRepositoryInterface) -> DeleteUserUseCaseInterface:
        """
        Fixture that sets up the DeleteUserUseCase with a mocked UserRepository.

        Args:
        user_repository (UserRepositoryInterface): The UserRepository fixture.

        Returns:
        delete_user_use_case (DeleteUserUseCaseInterface): An instance of DeleteUserUseCase with the mock UserRepository.
        """
        delete_user_use_case = DeleteUserUseCase(user_repository=user_repository)
        return delete_user_use_case

    def test_delete_user_successful_deletion(
        self,
        delete_user_use_case: DeleteUserUseCaseInterface,
        user_dto: UserDTO,
        mocker: MockerFixture,
    ):
        """
        Test the successful deletion of a user by the DeleteUserUseCase.

        Args:
            delete_user_use_case (DeleteUserUseCaseInterface): An instance of the DeleteUserUseCase.
            user_dto (UserDTO): The UserDTO representing the user to be deleted.
            mocker (MockerFixture): The MockerFixture for creating mocks and spies.

        """
        delete_user_use_case.user_repository.get_user_by_id.return_value = user_dto

        mock_delete_user_method = mocker.patch.object(delete_user_use_case.user_repository, "delete_user")
        response = delete_user_use_case.delete_user(user_id=user_dto.id)

        mock_delete_user_method.assert_called_once_with(user_id=user_dto.id)
        assert response == {"data": UserSuccessEnum.DELETE_SUCCESS.value, "success": True}

    def test_delete_user_do_not_found_a_user(
        self,
        delete_user_use_case: DeleteUserUseCaseInterface,
        user_dto: UserDTO,
    ):
        """
        Test the scenario when attempting to delete a non-existent user.

        Args:
            delete_user_use_case (DeleteUserUseCaseInterface): An instance of the DeleteUserUseCase.
            user_dto (UserDTO): The UserDTO representing the user to be deleted.
        """
        # Arrange
        delete_user_use_case.user_repository.get_user_by_id.return_value = None

        # Act
        response = delete_user_use_case.delete_user(user_id=user_dto.id)

        # Assert
        assert response == {"data": UserErrorsEnum.READ_NOT_FOUND.value, "success": False}
