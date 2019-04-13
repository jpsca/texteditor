all: PHONY

help:
	@echo "clean - remove build/python artifacts"
	@echo "test - run tests"
	@echo "flake - check style with flake8"
	@echo "install - install for development"
	@echo "publish - publish a new version"

clean: clean-build clean-pyc

clean-build:
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info
	rm -rf pip-wheel-metadata

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -rf {} +
	find . -name '.pytest_cache' -exec rm -rf {} +
	find . -name '*.egg-info' -exec rm -rf {} +

test:
	pytest -x texteditor.py tests.py

flake:
	flake8 --config=setup.cfg texteditor.py tests.py

install:
	pip install -e .
	pip install -r requirements-dev.txt

publish:
	python setup.py install
	python publish.py