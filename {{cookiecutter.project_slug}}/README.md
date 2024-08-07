# {{cookiecutter.project_name}}

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

### Configure your `.env`

After executing the `make install` command, you will enter the virtual environment of Poetry and find a `.env` configuration file under the project. Before starting the project, please complete the configuration first.

For more configurations, please check [HERE](src/app/core/config.py)

## Runnning

Start your system with the following command:

```sh
poetry run
```

### Testing

The `check` command only performs static checks on the code, including syntax and import checks. The `test` command will perform unit testing. Alternatively, you can choose `check-test` to run them together

```sh
poetry check
poetry test
poetry check-test
```

### Cleaning Cache

```sh
poetry clean
```

## Access Swagger Documentation

> <http://localhost:8080/docs>

The system defaults to starting on port `8000`, or you can modify this value in the configuration file

## Project Structure

Files related to application are in the `src` or `tests` directories.

Overall includes:

    Project
    ├── src
    │   ├── app
    │   │   ├── api
    │   │   │   ├── api.py
    │   │   │   ├── __init__.py
    │   │   │   └── routes
    │   │   │       ├── eventgpt.py
    │   │   │       └── __init__.py
    │   │   ├── core
    │   │   │   ├── config.py
    │   │   │   ├── errors.py
    │   │   │   ├── events.py
    │   │   │   ├── __init__.py
    │   │   │   └── logging.py
    │   │   ├── __init__.py
    │   │   ├── models
    │   │   │   ├── eventgpt.py
    │   │   │   └── __init__.py
    │   │   └── services
    │   │       ├── eventgpt.py
    │   │       └── __init__.py
    │   ├── __init__.py
    │   ├── main.py
    │   ├── service
    │   │   ├── __init__.py
    │   │   ├── openapi_model.py
    │   │   └── prompts
    │   │       └── eventgpt_prompt.yaml
    │   └── utils
    │       ├── __init__.py
    │       └── util.py
    └── tests
        ├── api
        │   ├── __init__.py
        │   └── test_eventgpt.py
        ├── conftest.py
        └── __init__.py
