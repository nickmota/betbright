#!/usr/bin/env python
# -*- coding: utf-8 -*-
import collections
from functools import wraps


def lru_cache(max_size=100):

    def deco_function(function):
        _cache = collections.OrderedDict()
        CacheInfo = collections.namedtuple('CacheInfo', 'hits misses max_size')

        @wraps(function)
        def wrapper(*args, **kwargs):
            key = args
            if kwargs:
                key += tuple(sorted(kwargs.items()))

            try:
                result = _cache.pop(key)
                wrapper.hits += 1
            except KeyError:
                result = function(*args, **kwargs)
                wrapper.misses += 1

                if len(_cache) >= max_size:
                    _cache.popitem(0)

            _cache[key] = result
            wrapper.cache_info = CacheInfo(
                hits=wrapper.hits,
                misses=wrapper.misses,
                max_size=max_size
            )
            return result

        wrapper.hits = 0
        wrapper.misses = 0

        return wrapper

    return deco_function


