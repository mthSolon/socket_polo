FROM python:3.8

WORKDIR /server

COPY server ./server

ENV VENV_PATH="/opt/venv/bin:$PATH"

RUN python -m venv "${VENV_PATH}"

COPY requirements.txt ./
# RUN pip install requirements.txt