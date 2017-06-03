#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
from random import choice
from betbright.lru.lru_decorator import lru_cache


def orig(x, y):
    return 3*x+y


class TestLRU(unittest.TestCase):
    f_count = 0

    def test_lru_should_return_cache_infos(self):
        f = lru_cache(max_size=20)(orig)

        hits, misses, max_size = f.cache_info

        self.assertEqual(max_size, 20)
        self.assertEqual(hits, 0)
        self.assertEqual(misses, 0)

    def test_lru_should_return_expected_value(self):
        
        f = lru_cache(max_size=20)(orig)

        domain = range(5)

        for i in range(100):
            x, y = choice(domain), choice(domain)
            actual = f(x, y)
            expected = orig(x, y)
            self.assertEqual(actual, expected)

        hits, misses, max_size = f.cache_info

        self.assertTrue(hits > misses)
        self.assertEqual(hits + misses, 100)

    def test_lru_with_size_zero(self):

        @lru_cache(0)
        def f():
            self.f_count += 1
            return 20

        self.assertEqual(f.cache_info.max_size, 0)

        self.f_count = 0

        for i in range(5):
            self.assertEqual(f(), 20)

        self.assertEqual(self.f_count, 5)

        hits, misses, max_size = f.cache_info

        self.assertEqual(hits, 0)
        self.assertEqual(misses, 5)

    def test_lru_with_size_one(self):

        @lru_cache(1)
        def f():
            self.f_count += 1
            return 20

        self.assertEqual(f.cache_info.max_size, 1)

        self.f_count = 0

        for i in range(5):
            self.assertEqual(f(), 20)

        self.assertEqual(self.f_count, 1)

        hits, misses, max_size = f.cache_info

        self.assertEqual(hits, 4)
        self.assertEqual(misses, 1)

    def test_lru_with_size_two(self):

        @lru_cache(2)
        def f(x):
            self.f_count += 1
            return x*10

        self.assertEqual(f.cache_info.max_size, 2)
        self.f_count = 0
        for x in [7, 9, 7, 9, 7, 9, 8, 8, 8, 9, 9, 9, 8, 8, 8, 7]:
            self.assertEqual(f(x), x*10)

        self.assertEqual(self.f_count, 4)

        hits, misses, max_size = f.cache_info

        self.assertEqual(hits, 12)
        self.assertEqual(misses, 4)


    def test_lru_with_maxsize_none(self):
        with self.assertRaises(TypeError):
            @lru_cache(max_size=None)
            def fib(n):
                if n < 2:
                    return n
                return fib(n-1) + fib(n-2)
            fib(10)

