# Api Routers

This document explains the purpose and configuration of the `router` of the School Platform API.

## Router Setup

The code snippet below demonstrates the setup of the `router` using the `APIRouter` class from FastAPI:

```python
from fastapi import APIRouter

from src.main.fast_api.routers import users
from src.main.fast_api.routers import swagger_api

router = APIRouter()

router.include_router(swagger_api.router, prefix="", tags=["Swagger Redirect"])
router.include_router(users.router, prefix="/users", tags=["User"])
```

## Purpose

The router setup serves as a crucial component for organizing and managing API routes within the School Platform application. It utilizes the `APIRouter` class from FastAPI to define and include various route modules.

## Breakdown

- `from fastapi import APIRouter`: This imports the `APIRouter` class from the FastAPI library, allowing the creation of a modular router for handling API routes.

- `router = APIRouter()`: An instance of `APIRouter` named `router` is created to manage the grouping and inclusion of different route modules.

- `router.include_router(swagger_api.router, prefix="", tags=["Swagger Redirect"])`: This line includes the `swagger_api` module's router, enabling redirection to Swagger API documentation. The `prefix` parameter is set to an empty string to indicate the root path, and the route is tagged under "Swagger Redirect."

- `router.include_router(users.router, prefix="/users", tags=["User"])`: This line includes the `users` module's router, providing routes related to user management. The `prefix` parameter is set to "/users," indicating that these routes will be available under the "/users" path. The route is tagged under "User."

## Conclusion

The router setup centralizes the management of API routes by utilizing the `APIRouter` class. It enables organized inclusion of various route modules, such as the Swagger API redirection and user-related routes, enhancing the overall structure and maintainability of the School Platform API.
