FROM python:3.8

WORKDIR /client

COPY client ./client

ENV POETRY_VERSION=1.2.2 \
    POETRY_HOME="/opt/poetry" \
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    POETRY_NO_INTERACTION=1\
    VENV_PATH="/opt/venv/bin:$PATH"

ENV PATH="$POETRY_HOME/bin:$VENV_PATH/bin:$PATH"

RUN python -m venv "${VENV_PATH}"
RUN pip install "poetry==${POETRY_VERSION}"

COPY pyproject.toml poetry.lock README.md ./
RUN poetry install