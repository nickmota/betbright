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

run-date-calculation:
	@python -m lottery.lottery_draw $(date_time)

run-find-anagram:
	@python -m anagram.find_anagram

run-lru:
	@python -m lru.lru


flake8:
	@flake8 --show-source .
