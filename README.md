# cookiecutter-fastapi

This is a template that can help you quickly develop the fastAPI backend. You only need a few easy steps to build a basic framework.

## What is Cookiecutter?

Cookiecutter is a CLI tool (Command Line Interface) to create an application boilerplate from a template. It uses a templating system — Jinja2 — to replace or customize folder and file names, as well as file content.

## What's Included in the Template?

Cookiecutter-fastapi is a template designed for rapid development of FastAPI-based backend services. It provides a basic LLM Agent system out of the box, while integrating a modern development toolchain with uv, MyPy, PyTest, Ruff, pre-commit, and Docker to streamline backend development and deployment.

This project is a backend development template built with **FastAPI**. It provides a basic LLM Agent system out of the box, including:

- User authentication
- Agent tool invocation
- Streaming conversations
- Multi-turn conversations
- Memory management.

The template uses **uv** for dependency management and integrates a complete development toolchain, covering project testing, static analysis and code auditing, code quality checks, GitHub CI workflows, and containerized deployment.

The included tools and technologies mainly consist of FastAPI, LLama-index, uv, PyTest, MyPy, Ruff, Poethepoet, Pre-commit, Docker, Docker Compose, SQLModel and Sqlacodegen.

## Quick Start

**Install Cookiecutter First**

```sh
pip install cookiecutter
```

**Generate a FastAPI Project**

```sh
cookiecutter https://github.com/tropical-algae/cookiecutter-fastapi.git
```

![image](https://github.com/tropical-algae/cookiecutter-fastapi/blob/main/asset/example.png)

For details on the base system architecture and usage, please refer to the project’s README after generating the template.