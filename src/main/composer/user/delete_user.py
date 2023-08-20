from src.applications.use_cases.user.delete_user import DeleteUserUseCase
from src.infra.db.settings.connection import DBConnectionHandler
from src.infra.repositories.user import UserRepository
from src.domain.controller import ControllerInterface
from src.presenters.controllers.user.delete_user import DeleteUserController


def delete_user_composer() -> ControllerInterface:
    """
    Compose the necessary components for deleting a user account route.

    This function creates and configures the required components to handle incoming
    HTTP requests for deleting user accounts. It establishes a connection to the
    database, initializes the user repository, sets up the delete user use case, and
    associates it with the appropriate controller.

    Returns:
        delete_user_controller (ControllerInterface): An instance of the DeleteUserController configured for deleting user accounts.
    """
    repository = UserRepository(db_connection=DBConnectionHandler())
    delete_user_use_case = DeleteUserUseCase(user_repository=repository)
    delete_user_controller = DeleteUserController(delete_user_use_case=delete_user_use_case)
    return delete_user_controller
