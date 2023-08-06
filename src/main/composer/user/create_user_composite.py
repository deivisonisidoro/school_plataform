from src.applications.use_cases.user.create_user import CreateUserUseCase
from src.infra.db.settings.connection import DBConnectionHandler
from src.infra.repositories.user import UserRepository
from src.main.interfaces.route import RouteInterface
from src.presenters.controllers.user.create_user_controller import CreateUserController


def create_user_composer() -> RouteInterface:
    """
    Compose the necessary components for creating a new user account route.

    This function creates and configures the required components to handle incoming
    HTTP requests for creating new user accounts. It establishes a connection to the
    database, initializes the user repository, sets up the create user use case, and
    associates it with the appropriate controller.

    Returns:
        create_user_controller (RouteInterface): An instance of the CreateUserController configured for creating new user accounts.
    """
    repository = UserRepository(db_connection=DBConnectionHandler())
    create_user_use_case = CreateUserUseCase(user_repository=repository)
    create_user_controller = CreateUserController(create_user_use_case=create_user_use_case)
    return create_user_controller
