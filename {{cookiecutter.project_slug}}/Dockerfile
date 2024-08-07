FROM python:3.10.14

ARG WORKSPACE=/workspace

WORKDIR ${WORKSPACE}

COPY poetry.lock pyproject.toml poetry.toml .env ./

RUN pip install --upgrade pip && \
    pip install poetry && \
    poetry config virtualenvs.create false

RUN poetry install --only main && poetry shell

COPY ./src ./src

ENV PYTHONPATH ${WORKSPACE}

EXPOSE 8000

CMD python ${WORKSPACE}/src/main.py
