FROM python:3.10-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY . /app/

RUN pip install --no-cache-dir poetry
RUN poetry config virtualenvs.create false
RUN poetry install --no-root --no-dev

EXPOSE 8000

CMD ["poetry", "run", "uvicorn", "src.infra.fast_api.server:app", "--host", "0.0.0.0", "--port", "8000"]
