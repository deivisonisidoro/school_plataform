from datetime import datetime
from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session

from src.applications.dtos.user import UserDTO
from src.applications.use_cases.user.create_user import CreateUserUseCase
from src.applications.use_cases.user.get_user_by_email import GetUserByEmailUseCase

from src.infra.db.relational_db import get_db
from src.infra.fast_api.schemas import UserCreate, UserOut
from src.infra.fast_api.schemas.default_response import DefaultResponse
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


@router.get(
    "/{email}",
    status_code=status.HTTP_200_OK,
    response_model=DefaultResponse,
    summary="Get user by email",
    description="Retrieve a user by their email.",
)
def get_user_by_email(email: str, db: Session = Depends(get_db)):
    """
    Retrieve a user by their email.

    This endpoint allows fetching a user from the database based on their email.

    Parameters:
        email (str): The email of the user to retrieve.

    Returns:
        User: The user details if found.

    """
    user_repository = UserRepository(db=db)
    get_user_use_case = GetUserByEmailUseCase(user_repository=user_repository)
    user = get_user_use_case.get_user(email)
    detail = user.get("detail")
    status_code = user.get("status_code")
    if status_code != 200:
        raise HTTPException(status_code=status_code, detail=user.get("detail"))
    user_out = UserOut(
        id=detail.id,
        email=detail.email,
        name=detail.name,
        created_at=detail.created_at,
    )

    return DefaultResponse(detail=user_out, status_code=status_code)
