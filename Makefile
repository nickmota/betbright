test: 
	py.test -v -x

install:
	@pip install -r requirements.txt --upgrade

run-date-calculation:
	@python -m lottery.lottery_draw $(date_time)

run-find-anagram:
	@python -m anagram.find_anagram

run-lru:
	@python -m lru.lru
