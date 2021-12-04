test:
	pytest -x texteditor tests

lint:
	flake8 --config=setup.cfg texteditor tests

coverage:
	pytest --cov-report html --cov texteditor texteditor tests

typecheck:
	mypy texteditor tests

setup:
	pip install -U pip wheel
	pip install -e .[dev,test]
	pre-commit install
