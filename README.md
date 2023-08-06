# School Platform

Welcome to the School Platform project! This platform aims to facilitate the creation of school platforms using the Clean Architecture approach. The project is structured into three main folders within the `src` directory: `application`, `infra`, and `domain`. It utilizes several technologies and tools, including SQLAlchemy, FastAPI, Poetry, pylint, flake8, black, and pre-commit.

## Project Structure

The School Platform project follows the principles of Clean Architecture to ensure a clear separation of concerns and maintainability. Here's a brief overview of each folder's purpose:

### 1. `src/application`

The `application` folder contains the core business logic and use cases of the School Platform. It should be independent of any external frameworks or libraries. Here, you'll find the application's use cases, business rules, and application services.

### 2. `src/infra`

The `infra` folder deals with infrastructure concerns, including database interactions, external API implementations, and other external services. It houses the implementations for data access, data repositories, and other external interfaces.

### 3. `src/domain`

The `domain` folder holds the domain models and entities of the School Platform. It defines the core data structures and business logic representations, providing the foundation for the entire application.

## Technologies and Tools

The School Platform project utilizes the following technologies and tools:

### - SQLAlchemy

SQLAlchemy is used for interacting with the database and managing data persistence. It provides an ORM (Object-Relational Mapping) to map Python classes to database tables and enables seamless database operations.

### - FastAPI

FastAPI is the web framework of choice for building the School Platform's API. It is a high-performance web framework based on Python type hints, allowing for automatic validation and documentation of API endpoints.

### - Poetry

Poetry is used as the package manager for the project. It simplifies dependency management and project building, making it easier to manage project dependencies and environments.

### - pylint

Pylint is a static code analysis tool that helps identify and report programming errors, bugs, and stylistic issues in Python code. It enforces code quality and adheres to Python's coding standards.

### - flake8

Flake8 is another code linting tool that checks your Python code against coding style guidelines. It complements pylint and helps maintain consistent and clean code throughout the project.

### - black

Black is an opinionated code formatter that automatically formats Python code to adhere to a consistent style. It helps maintain a uniform and readable codebase.

### - pre-commit

Pre-commit is a useful tool for managing and maintaining pre-commit hooks. These hooks can perform various tasks such as code linting, formatting, and testing before each commit, ensuring that only clean and validated code gets committed.

## Getting Started

To get started with the School Platform project, follow these steps:

1. **Clone the repository**: Start by cloning the project repository from GitHub using the following command:

```bash
git clone https://github.com/deivisonisidoro/school_plataform.git
```
2. **Install dependencies using Poetry**: Move into the project directory and install the required dependencies with Poetry:
```bash
cd school_plataform
poetry install
 ```
3. **Database Configuration**: Set up your database configuration by creating a .env file in the root directory of the project. You can use the provided .env.example file as a template.
4. **Run the FastAPI server**: `poetry run uvicorn src.main.fast_api.configs.server:app --reload`

Ensure you have the required Python version installed as specified in the `pyproject.toml` file.

## Contributing

We welcome contributions to the School Platform project. If you find any issues or want to add new features, feel free to open a pull request. Make sure to follow the coding standards and run the pre-commit hooks before committing your changes.

Before submitting a pull request, run the following command to ensure your code meets the project's standards:
```bash
poetry run pre-commit run --all-files
 ```

