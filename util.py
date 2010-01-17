#!/usr/bin/python

# Implementation of lots of crazy evaluation functions.
def root_vegetables(s):
    return iter(['carrot', 'potato'])

def at_least_three_letters_at_least_twice(s):
    count = 0
    seen = set()
    for letter in s:
        if letter in seen:
            count += 1
        seen.add(letter)
    return count >= 3
