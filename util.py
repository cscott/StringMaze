#!/usr/bin/python

# Implementation of lots of crazy evaluation functions.
def is_root_vegetable(s):
    return s in ['carrot', 'potato'] # XXX more?

def at_least_three_letters_at_least_twice(s):
    count = 0
    seen = set()
    for letter in s:
        if letter in seen:
            count += 1
        count.add(letter)
    return count >= 3
