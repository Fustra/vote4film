# Vote4Film

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)


Simplify film selection for regular film nights.

## Development

1. `poetry install` to set-up the virtualenv (one-off)
2. `poetry run ./src/vote4film/manage.py migrate` to set-up the local DB (one-off)
3. `poetry run ./src/vote4film/manage.py runserver_plus`
4. `make check` and `make test` before committing

### Publishing

This application will be published on PyPi.

## Deployment

Unfortunately, I will not provide any guidance here.
