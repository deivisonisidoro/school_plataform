# Server

This document explains the purpose and components of the `server.py` file, which sets up the School Platform API using FastAPI.

## Overview

The `server.py` file is the entry point for the School Platform API. It imports required libraries and modules and sets up the API using FastAPI.

## Code Breakdown

### Import Statements

The following import statements bring in necessary modules:

```python
import os
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.main.fast_api.routers.api_routers import router
```

- `os` and `load_dotenv` are used to load environment variables from the `.env` file.

- `FastAPI` is imported to create the API application.

- `CORSMiddleware` is used to handle Cross-Origin Resource Sharing (CORS).

- `router` is imported from `api_routers` to include the API routes.

### Create FastAPI Instance

A FastAPI instance named `app` is created with the following configuration:

```python
app = FastAPI(
    title="School Platform API",
    version="0.0.1",
    docs_url="/swagger/doc",
    redoc_url="/swagger/redoc",
)
```

- `title` and `version` specify the API's title and version.
- `docs_url` and `redoc_url` define the URLs for Swagger documentation and ReDoc.

## CORS Middleware

The following code sets up CORS middleware to allow requests from specified origins:

```python
origins = ["http://localhost:3000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

## Include API Routes

The API routes are included using the following code:

```python
app.include_router(router, prefix="/api")
```
- `router` contains the API routes defined in the `api_routers` module.

## Conclusion

The server.py file serves as the starting point for the School Platform API. It sets up the API using FastAPI, configures CORS, and includes the defined API routes for further processing.

