#!/usr/bin/env python
# -*- coding: utf-8 -*-
import collections
from functools import wraps
from itertools import ifilterfalse


class Count(dict):
    def __missing__(self, key):
        return 0

def lru_cache(max_size=100):

    if not isinstance(max_size, int):
        raise TypeError("Invalid max_size parameter. Integer expected")

    max_queue = max_size * 10
    def deco_function(function):
        queue = collections.deque()
        CacheInfo = collections.namedtuple(
            'CacheInfo',
            'hits misses max_size'
        )
        _cache = {}
        occu_count = Count() 
        watchman = object()
        kwargs_position = object()
        
        @wraps(function)
        def wrapper(*args, **kwargs):
            key = args
            if kwargs:
                key += (kwargs_position,) + tuple(sorted(kwargs.items()))
            queue.append(key)
            occu_count[key] += 1

            try:
                result = _cache[key]
                wrapper.hits += 1
            except KeyError:
                result = function(*args, **kwargs)
                _cache[key] = result
                wrapper.misses += 1

                if len(_cache) > max_size:
                    key = queue.popleft()
                    occu_count[key] -= 1
                    while occu_count[key]:
                        key = queue.popleft()
                        occu_count[key] -= 1
                    del _cache[key], occu_count[key]

            if len(queue) > max_queue:
                occu_count.clear()
                queue.appendleft(watchman)
                for key in ifilterfalse(
                    occu_count.__contains__,
                    iter(queue.pop, watchman)
                ):
                    queue.appendleft(key)
                    occu_count[key] = 1

            wrapper.cache_info = CacheInfo(
                hits=wrapper.hits,
                misses=wrapper.misses,
                max_size=max_size
            )
            return result

        def clear():
            _cache.clear()
            queue.clear()
            occu_count.clear()
            wrapper.hits = 0
            wrapper.misses = 0

        wrapper.hits = 0
        wrapper.misses = 0
        wrapper.clear = clear
        wrapper.cache_info = CacheInfo(
            hits=wrapper.hits,
            misses=wrapper.misses,
            max_size=max_size
        )
        return wrapper

    return deco_function
