from fastapi import APIRouter, status, Request, HTTPException

from src.main.adapter import fast_api_adapter
from src.main.composer.user import get_user_composer, create_user_composer
from src.main.fast_api.schemas import UserCreate, UserOut, DefaultResponse

router = APIRouter()


@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    summary="Create a new user",
    description="Create a new user with the provided data in the request body.",
    response_model=DefaultResponse,
)
def create_user(user: UserCreate, request: Request):
    """
    Create a new user.

    This endpoint allows creating a new user with the provided data in the request body.
    The response will include the details of the created user.

    Args:
        user (UserCreate): The user creation data from the request body.
        request (Request): The HTTP request object.

    Returns:
        dict: A dictionary containing the details of the created user.
    """
    request.json = user.__dict__
    response = fast_api_adapter(request=request, api_route=create_user_composer())
    if response.status_code != status.HTTP_201_CREATED:
        raise HTTPException(status_code=response.status_code, detail=response.body)

    user_out = UserOut(
        id=response.body.id,
        email=response.body.email,
        name=response.body.name,
        created_at=response.body.created_at,
    )
    return DefaultResponse(type="Users", attributes=user_out)


@router.get(
    "/",
    status_code=status.HTTP_200_OK,
    summary="Get user by email",
    description="Retrieve a user by their email.",
)
def get_user(request: Request):
    """
    Retrieve a user by their email.

    This endpoint retrieves a user's details by their email address.

    Args:
        request (Request): The HTTP request object.

    Returns:
        dict: A dictionary containing the details of the retrieved user.
    """
    response = fast_api_adapter(request=request, api_route=get_user_composer())
    if response.status_code != status.HTTP_200_OK:
        raise HTTPException(status_code=response.status_code, detail=response.body)

    user_out = UserOut(
        id=response.body.id,
        email=response.body.email,
        name=response.body.name,
        created_at=response.body.created_at,
    )
    return DefaultResponse(type="Users", attributes=user_out)
