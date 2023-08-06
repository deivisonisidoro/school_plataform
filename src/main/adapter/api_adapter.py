from src.main.interfaces.route import RouteInterface
from src.presenters.helpers.http_types import HttpRequest, HttpResponse


def fast_api_adapter(request: any, api_route: RouteInterface) -> HttpResponse:
    """Adapter function to process a FastAPI request and call the corresponding API route.

    Args:
        request (any): The FastAPI request object.
        api_route (RouteInterface): The API route implementation that handles the request.

    Returns:
        response (HttpResponse): The response data returned by the API route.
    """
    http_request = HttpRequest(query=request.query_params, body=request.json, header=request.headers)
    response = api_route.route(http_request=http_request)
    return response
