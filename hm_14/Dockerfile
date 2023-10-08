FROM ubuntu:latest
LABEL authors="Yaroslav Melnychuk <yarmel.dev@gmail.com>"

RUN apt-get update && apt-get install -y python3-pip
RUN pip install uvicorn
RUN pip install poetry

COPY pyproject.toml poetry.lock /app/
WORKDIR /app
RUN poetry config virtualenvs.create false && poetry install --no-interaction --no-ansi

COPY . /app

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
