FROM python:3.11-slim

ENV PYTHON_VERSION=3.11.8 \
  APP_PATH=/home/python/app \
  POETRY_VIRTUALENVS_CREATE=false \
  PATH=/home/python/.local/lib/python3.11/site-packages:/usr/local/bin:/home/python:/home/python/app/bin:$PATH

RUN apt-get update -y && apt-get upgrade -y && apt-get install -y gcc \
    gettext postgresql-client libpq-dev libjpeg-dev libopenjp2-7-dev

RUN pip install --no-cache-dir poetry

RUN mkdir /app/
WORKDIR /app/
RUN pip install pip -U && pip install poetry -U
RUN poetry config virtualenvs.create false


COPY ../../pyproject.toml /app/.
COPY ../../poetry.lock /app/.
RUN poetry install

VOLUME [ "/app/" ]

#CMD ["tail", "-f", "/dev/null"]
