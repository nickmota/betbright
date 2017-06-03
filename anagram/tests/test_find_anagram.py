#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from ..find_anagram import find_anagrams


class TestFindAnagrams(unittest.TestCase):

    def test_should_find_anagram_with_list_arg(self):
        result = find_anagrams('roma', ['amor', 'teste', 'mora'])
        self.assertEqual(len(result), 2)

    def test_should_find_anagram_with_special_chars(self):
        result = find_anagrams('leão', ['oãel', '', 'mora', 'ãããos'])
        self.assertEqual(len(result), 1)

    def test_should_find_anagram_with_tuple_arg(self):
        result = find_anagrams('leão', ('oãel', '', 'mora', 'ãããos'))
        self.assertEqual(len(result), 1)

    def test_should_find_anagram_with_empty_string(self):
        result = find_anagrams('', ('oãel', '', 'mora', 'ãããos'))
        self.assertEqual(len(result), 1)

    def test_should_find_anagram_with_number_on_string(self):
        result = find_anagrams(1, ('oãel', '', 'mora', 'ãããos'))
        self.assertFalse(result)
