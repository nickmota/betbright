#!/usr/bin/env python
# -*- coding: utf-8 -*-

from ..find_anagram import find_anagrams


class TestFindAnagrams(object):

    def test_should_find_anagram(self):
        result = find_anagrams('roma', ['amor', 'teste', 'mora'])
        assert len(result) == 2