#!/usr/bin/python
from __future__ import with_statement

# read in dictionary
FILENAME='/usr/share/dict/web2'

_dict_words = set()
_anagrams = set()

def _sorted_letters(s):
    return ''.join(sorted(s))

with open(FILENAME) as f:
    for line in f.readlines():
        word = line.strip().lower()
        _dict_words.add(word)
        _anagrams.add(_sorted_letters(word))

def mw_entry():
    return iter(_dict_words)

def is_anagram(s):
    return _sorted_letters(s) in _anagrams
