from fastapi import APIRouter
from fastapi.responses import RedirectResponse

router = APIRouter()


@router.get(
    "/",
    summary="Redirect to API Documentation",
    description="Redirects to the Swagger API documentation page.",
    response_class=RedirectResponse,
)
def redirect_api_documentation():
    """
    Redirect to API Documentation.

    This endpoint redirects the user to the Swagger API documentation page.
    The Swagger UI provides a user-friendly interface to explore and interact with the API endpoints.

    Returns:
        (RedirectResponse): A redirect response to the Swagger API documentation page.

    """
    return RedirectResponse(url="/swagger/doc")
