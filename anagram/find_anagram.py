#!/usr/bin/env python
# -*- coding: utf-8 -*-


def find_anagrams(string, list_anagrams):
    '''
        Find anagrams in list with word received in string
        params:
        string: Word that will be found its anagrams
        list_anagrams: A list or tuple with words that will be 
        compared to the string
    '''
    sorted_string = sorted(str(string))
    list_of_results = [
        word
        for word in list_anagrams if sorted(str(word)) == sorted_string
    ]
    return list_of_results


if __name__ == '__main__':
    string = 'test'
    list_test = ['tesst', 'tset', 'ttse', 'sets']
    list_anagrams = find_anagrams(string, list_test)
    print 'List of Anagrams with word "{}": {}'.format(
        string,
        list_anagrams
    )
