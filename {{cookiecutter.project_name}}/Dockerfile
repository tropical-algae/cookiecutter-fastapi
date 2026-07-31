FROM python:3.13-slim

COPY --from=ghcr.io/astral-sh/uv:0.11.21 /uv /uvx /bin/

LABEL org.opencontainers.image.authors="{{cookiecutter.author_name}} {{cookiecutter.email}}"

ARG WORKSPACE=/app

WORKDIR ${WORKSPACE}


RUN apt-get update && \
    apt-get install -y --no-install-recommends ripgrep && \
    rm -rf /var/lib/apt/lists/*

COPY pyproject.toml uv.lock poe_tasks.toml README.md ./

RUN uv sync --frozen --no-default-groups --no-install-project

COPY ./src ./src

RUN uv sync --frozen --no-default-groups --no-editable

ENV PYTHONPATH ${WORKSPACE}

EXPOSE 8000

CMD ["uv", "run", "python", "-m", "{{cookiecutter.project_slug}}.main"]
