<p align="center">
  <img alt="App" src="https://github.com/fiufit/app/assets/86434696/82a49b69-d7bd-4f7d-9449-79b8b60335b1" height="200" />
</p>


# FiuFit: Gateway

[![Fly Deploy](https://github.com/fiufit/gateway/actions/workflows/fly.yml/badge.svg?branch=main)](https://github.com/fiufit/gateway/actions/workflows/fly.yml)

[![Black format](https://github.com/fiufit/gateway/actions/workflows/python-black.yml/badge.svg?branch=main)](https://github.com/fiufit/gateway/actions/workflows/python-black.yml)
[![Flakeheaven Linter](https://github.com/fiufit/gateway/actions/workflows/python-flake.yml/badge.svg?branch=main)](https://github.com/fiufit/gateway/actions/workflows/python-flake.yml)

[![codecov](https://codecov.io/gh/fiufit/gateway/branch/main/graph/badge.svg?token=NRRA48UTP5)](https://codecov.io/gh/fiufit/gateway)
[![Tests](https://github.com/fiufit/gateway/actions/workflows/python-app.yml/badge.svg?branch=main)](https://github.com/fiufit/gateway/actions/workflows/python-app.yml)

API gateway or BFF for FiuFit's microservice structure

## Installing the project

This project was build with [poetry](https://python-poetry.org/docs/) to manage dependencies.

Having poetry installed, run this command to install the dependencies:

```
poetry install
```

## Dev

To add new dependencies, you can run:

```
poetry add <dependency>
```

**NOTE**: Don't forget to commit all changes to `poetry.lock` and `pyproject.toml`! 

To activate the virtual environment run:

```
poetry shell
```

Then, you can run the app using:

```
python src/main.py
```

To run the formatter:

```
black [Options] path
```

To run the linter:

```
flakeheaven lint path
```

To run the tests:

```
pytest
```

If you want to check code coverage locally:

```
pytest --cov -v
```

Finally, you can exit the virtual environment:

```
exit
```

## Running locally

In addition to running it directly within poetry's virtual environment you can run the project with Docker:

* Create a `.env` file with the same environment variables as in `.example-env`

* Run `docker build -t fiufit-gateway .`

* Run `docker run -p PORT:PORT --env-file=.env fiufit-gateway`

## Links

- Fly.io deploy dashboard:

    - https://fly.io/apps/fiufit-gateway

- Swagger docs:

    - https://fiufit-gateway.fly.dev/docs

- Coverage report:

    - https://app.codecov.io/github/fiufit/gateway
