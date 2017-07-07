# Exercises

## Installation
- Create and activate a [virtualenv](https://virtualenv.pypa.io/) with python 2.7.
- Install the dependencies:

    `make install`

## Tests
- To run the tests, run:

    `make test`

## Running the questions:
- Date Calculation:

    `make run-date-calculation date_time="20-05-2017 10:00"`
    
    Ps: If date_time is not informed, the calculation will be done with the current date

- Least recently used cache

    `make run-lru`

- Find the anagram

    `make run-find-anagram`
