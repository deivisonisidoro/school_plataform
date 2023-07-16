import os

from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse
from src.infra.fast_api.routers import router
from src.infra.db.relational_db import Base, engine


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
load_dotenv(os.path.join(BASE_DIR, ".env"))

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="School Platform API",
    version="0.0.1",
    docs_url="/swagger/doc",
    redoc_url="/swagger/redoc",
)


origins = ["http://localhost:3000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get(
    "/",
    tags=["Doc Redirect"],
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
        RedirectResponse: A redirect response to the Swagger API documentation page.

    """
    return RedirectResponse(url="/swagger/doc")


app.include_router(router, prefix="/api")
