default: test

clean-pyc:
	@find . -iname '*.py[co]' -delete
	@find . -iname '__pycache__' -delete
	@find . -iname '.coverage' -delete
	@rm -rf htmlcov/

clean-dist:
	@rm -rf dist/
	@rm -rf build/
	@rm -rf *.egg-info

clean-tmp:
	@find ./ -name '*.pyc' -exec rm -f {} \;
	@find ./ -name 'Thumbs.db' -exec rm -f {} \;
	@find ./ -name '*~' -exec rm -f {} \;
	rm -rf .cache
	rm -rf build
	rm -rf dist
	rm -rf *.egg-info
	rm -rf htmlcov
	rm -rf .tox/
	rm -rf docs/_build
	rm -rf cover/
	rm -rf .coverage
	rm -rf .pytest_cache/

pip-local: 
	pip install -e .[dev] --upgrade --no-cache

clean: clean-pyc clean-dist clean-tmp

install: clean pip-local

test:
	pytest tests/ -v --cov=flapp

lint:
	SKIP=no-commit-to-branch pre-commit run -a -v