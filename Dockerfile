FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apt update && apt -y upgrade  && apt install -y curl

ENV POETRY_HOME="/opt/poetry" \
    POETRY_VERSION=1.7.0
ENV PATH="$POETRY_HOME/bin:$PATH"
RUN curl -sSL https://install.python-poetry.org | python3 -

RUN poetry config virtualenvs.create false


WORKDIR /gracias

COPY poetry.lock /gracias
COPY pyproject.toml /gracias
RUN poetry install --no-root

COPY . /gracias
EXPOSE 5000

CMD [ "flask",  "--app",  "app", "run", "-h" "0.0.0.0" "-p" "5000" ]