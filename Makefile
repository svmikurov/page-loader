install:
	poetry install

lint:
	poetry run flake8

test:
	poetry run pytest

test-coverage:
	poetry run pytest --cov=page_loader tests/ --cov-report xml

selfcheck:
	poetry check

check: selfcheck lint test

build:
	poetry build

package-install:
	python3 -m pip install --user dist/*.whl