# {{cookiecutter.project_slug}}

{{cookiecutter.project_short_description}}

## Development Requirements

- Ubuntu 20.04 / 22.04
- Python 3.10.14
- Pip
- Poetry (Python Package Manager)
- Make

## How to start?

Install poetry, download dependencies, and activate the poetry development environment through the following commands. We will create the virtual environment required for development under the project by default.

```sh
make install
```

To start from the terminal again, you need to activate the environment first:

```sh
make activate
```

### Configure your `.env`

Before starting the project, please complete the configuration first.

[.env.example](.env.example) is a sample configuration, for more configurations, please check [HERE](src/{{cookiecutter.project_slug}}/common/config.py)

### Runnning

Start your system with the following command:

```sh
poe run
```

### Testing

The `check` command only performs static checks on the code, including syntax and import checks. The `test` command will perform unit testing. Alternatively, you can choose `check-test` to run them together

```sh
poe check
poe test
poe check-test
```

### Cleaning Cache

```sh
poe clean
```

### Database visioning

Add the SQL table in part of 'update-db' in Makefile, then run this to generate code of table.

```sh
poe update-db
```

## Access Swagger Documentation

> <http://localhost:8080/docs>

The system defaults to starting on port `8000`, or you can modify this value in the configuration file

## Project Structure

Files related to application are in the `src` or `tests` directories.

Overall includes:

```
.
├── CHANGELOG.md
├── Dockerfile
├── Makefile
├── README.md
├── asset
│   └── prompts
│       └── eventgpt_prompt.yaml
├── docker-compose.yml
├── mypy.ini
├── poe_tasks.toml
├── poetry.lock
├── poetry.toml
├── pyproject.toml
├── pytest.ini
├── ruff.toml
├── semantic.toml
├── src
│   └── {{cookiecutter.project_slug}}
│       ├── __init__.py
│       ├── app
│       │   ├── __init__.py
│       │   ├── api
│       │   │   ├── __init__.py
│       │   │   ├── deps.py
│       │   │   ├── endpoints
│       │   │   │   ├── __init__.py
│       │   │   │   ├── eventgpt.py
│       │   │   │   └── user.py
│       │   │   └── routers.py
│       │   ├── db
│       │   │   ├── __init__.py
│       │   │   ├── crud
│       │   │   │   ├── __init__.py
│       │   │   │   └── crud_user.py
│       │   │   ├── models.py
│       │   │   └── session.py
│       │   ├── services
│       │   │   ├── __init__.py
│       │   │   └── eventgpt.py
│       │   └── utils
│       │       ├── __init__.py
│       │       ├── constant.py
│       │       ├── errors.py
│       │       ├── events.py
│       │       └── security.py
│       ├── common
│       │   ├── __init__.py
│       │   ├── config.py
│       │   ├── logging.py
│       │   ├── model
│       │   │   ├── __init__.py
│       │   │   ├── eventgpt.py
│       │   │   └── user.py
│       │   └── util.py
│       ├── core
│       │   ├── __init__.py
│       │   └── llm
│       │       ├── __init__.py
│       │       ├── base.py
│       │       └── eventgpt.py
│       └── main.py
└── tests
    ├── __init__.py
    ├── api
    │   ├── __init__.py
    │   ├── test_eventgpt.py
    │   └── test_user.py
    └── conftest.py


```