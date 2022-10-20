FROM python:3.8

WORKDIR /client

COPY client ./client

ENV VENV_PATH="/opt/venv/bin:$PATH"

ENV PATH="$POETRY_HOME/bin:$VENV_PATH/bin:$PATH"

RUN python -m venv "${VENV_PATH}"
COPY requirements.txt logos-1.jpg ifce.png ./
# RUN pip install requirements.txt