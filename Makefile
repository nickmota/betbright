clean:
	@find . -name "*.pyc" | xargs rm -rf
	@find . -name "*.pyo" | xargs rm -rf
	@find . -name "__pycache__" -type d | xargs rm -rf
	@rm -f .coverage
	@rm -rf htmlcov/
	@rm -f coverage.xml
	@rm -f *.log

fix-imports:
	git diff origin/master --name-only | grep py | xargs isort -ri

all-checks: fix-imports flake8 test

test: clean
	py.test -v -x

install:
	@pip install -r requirements.txt --upgrade

flake8:
	@flake8 --show-source .
