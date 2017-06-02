#!/usr/bin/env python
# -*- coding: utf-8 -*-

from ..find_anagram import find_anagrams


class TestFindAnagrams(object):

    def test_should_find_anagram_with_list_arg(self):
        result = find_anagrams('roma', ['amor', 'teste', 'mora'])
        assert len(result) == 2

    def test_should_find_anagram_with_special_chars(self):
        result = find_anagrams('leão', ['oãel', '', 'mora', 'ãããos'])
        assert len(result) == 1

    def test_should_find_anagram_with_tuple_arg(self):
        result = find_anagrams('leão', ('oãel', '', 'mora', 'ãããos'))
        assert len(result) == 1

    def test_should_find_anagram_with_empty_string(self):
        result = find_anagrams('', ('oãel', '', 'mora', 'ãããos'))
        assert len(result) == 1

    def test_should_find_anagram_with_number_on_string(self):
        result = find_anagrams(1, ('oãel', '', 'mora', 'ãããos'))
        assert not result
