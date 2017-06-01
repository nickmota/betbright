#!/usr/bin/env python
# -*- coding: utf-8 -*-


def find_anagrams(string, list_anagrams):
	list_of_results = []
	sorted_string = sorted(string)
	[list_of_results.append(word) for word in list_anagrams if sorted(word) == sorted_string]
	return list_of_results