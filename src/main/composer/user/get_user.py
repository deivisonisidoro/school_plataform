from src.domain.controllers import ControllerInterface
from src.infra.db.settings.connection import DBConnectionHandler
from src.presenters.controllers import GetUserController
from src.applications.use_cases.user.get_user import GetUserUseCase
from src.infra.repositories.user import UserRepository


def get_user_composer() -> ControllerInterface:
    """Return a ControllerInterface object for composing user routes.

    Returns:
        ControllerInterface: An object that implements the ControllerInterface interface
            for handling user routes.
    """
    repository = UserRepository(db_connection=DBConnectionHandler())
    get_user_use_case = GetUserUseCase(user_repository=repository)
    get_user_route = GetUserController(get_user_use_case=get_user_use_case)

    return get_user_route
