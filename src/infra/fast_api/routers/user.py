from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from datetime import datetime


from src.applications.dtos.user import UserDTO
from src.applications.use_cases.user.create_user import CreateUserUseCase

from src.infra.db.relational_db import get_db
from src.infra.fast_api.schemas import UserCreate, UserOut
from src.infra.repositories.user import UserRepository

router = APIRouter()


@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    response_model=UserOut,
    summary="Create a new user",
    description="Create a new user with the provided data.",
)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    """
    Create a new user.

    This endpoint allows creating a new user with the provided data in the request body.
    The response will include the created user details.

    Parameters:
        user (UserCreate): The user data for creating a new user.

    Returns:
        User: The created user details.

    """
    user_repository = UserRepository(db=db)
    user_create_use_case = CreateUserUseCase(user_repository=user_repository)
    user_dto = UserDTO(
        id=None,
        email=user.email,
        name=user.name,
        password=user.password,
        created_at=datetime.now(),
    )
    return user_create_use_case.create_user(user_dto)
