import requests

from .lru_decorator import lru_cache


@lru_cache(max_size=32)
def get_pep(num):
    url = 'http://www.python.org/dev/peps/pep-%04d/' % num
    try:
        response = requests.get(url)
        return response.ok
    except:
        return 'PEP Not Found'


@lru_cache(max_size=100)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)


if __name__ == '__main__':
    for n in range(10):
        pep = get_pep(n)
        print n, pep

    print get_pep.cache_info

    for n in range(32):
        fibonacci(n)

    print fibonacci.cache_info
