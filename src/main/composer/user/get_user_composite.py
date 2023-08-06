from src.infra.db.settings.connection import DBConnectionHandler
from src.main.interfaces import RouteInterface
from src.presenters.controllers import GetUserController
from src.applications.use_cases.user.get_user import GetUserUseCase
from src.infra.repositories.user import UserRepository


def get_user_composer() -> RouteInterface:
    """Return a RouteInterface object for composing user routes.

    Returns:
        RouteInterface: An object that implements the RouteInterface interface
            for handling user routes.
    """
    repository = UserRepository(db_connection=DBConnectionHandler())
    get_user_use_case = GetUserUseCase(user_repository=repository)
    get_user_route = GetUserController(get_user_use_case=get_user_use_case)

    return get_user_route
