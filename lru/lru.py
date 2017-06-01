#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Implement a least recently used (LRU) cache mechanism using a   
decorator and demonstrate it use in a small script. The LRU must be able    
to admit a ‘max_size’ parameter that by default has to be 100.    
"""

class LRUCache(object):

    def __init__(self, size):
        self.size = int(size)
        self.index = 0
        self.maxpos = size - 1
        self.keys = [None] * size
        self.refs = [False] * size
        self.data = {}

    def get(self, key, default=None):
        try:
            pos, val = self.data[key]
        except KeyError:
            return default
        self.refs[pos] = True
        return val

    def put(self, key, val):
        entry = self.data.get(key)
        if entry is not None:
            pos, old_val = entry
            if old_val is not val:
                data[key] = (pos, val)
            self.refs[pos] = True
            return

        while 1:
            ref = self.refs[self.index]
            if ref == True:
                self.refs[self.index] = False
                self.index += 1
                if self.index > self.maxpos:
                    self.index = 0
            else:
                oldkey = self.keys[self.index]
                oldentry = self.data.pop(oldkey, None)
                self.keys[self.index] = key
                self.refs[self.index] = True
                self.data[key] = (self.index, val)
                self.index += 1
                if self.index > self.maxpos:
                    self.index = 0
                break

class cache_it(object):

    def __init__(self, maxsize=100):
        self.cache = LRUCache(maxsize)

    def __call__(self, f):
        cache = self.cache

        def decorated(x):
            val = cache.get(x)
            if val is None:
                val = f(x)
                cache.put(x, val)
                action = 'put'
            else:
                action = 'get'
            return '%i - %s' % (val, action)
        
        setattr(decorated, '__module__', getattr(f, '__module__', f))
        setattr(decorated, '__name__', getattr(f, '__name__', f))
        setattr(decorated, '__doc__', getattr(f, '__doc__', f))
        
        decorated._cache = cache
        
        return decorated

@cache_it(3)
def _lru_cached_fn(x):
    return int(x)**2

if __name__ == '__main__':
    for x in '1133377335':
        print _lru_cached_fn(x)
