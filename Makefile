install:
    poetry install

gendiff:
    poetry run gendiff

build:
    poetry build
publish:
    poetry run flake8 gendiff

lint:
    poetry run flake8 gendiff

test:
    poetry run pytest