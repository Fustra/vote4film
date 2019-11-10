# Vote4Film

Simplify film selection for regular film nights.

This is a WSGI application.

## Development

1. `poetry install` to set-up the virtualenv (one-off)
2. `poetry run ./src/vote4film/manage.py migrate` to set-up the local DB (one-off)
3. `poetry run ./src/vote4film/manage.py runserver_plus`
4. `make check` and `make test` before committing

### Publishing

This application will be published on PyPi.

1. Ensure you have configured Poetry repositories including `TestPyPi`
2. Test the build with `poetry build`
3. `poetry publish --build -r testpypi` to upload to the test repository
4. `poetry publish --build` to release

## Deployment

Unfortunately, I will not provide any guidance here.
