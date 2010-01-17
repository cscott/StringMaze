#!/usr/bin/python
from __future__ import with_statement

# read in dictionary
FILENAME='/usr/share/dict/web2'

dict_words = set()

with open(FILENAME) as f:
    for line in f.readlines():
        dict_words.add(line.strip().lower())

def mw_entry():
    return iter(dict_words)
