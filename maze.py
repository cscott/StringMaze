#!/usr/bin/python

def default_bluebox(s): return True # any entry
def default_greenbox(s): return False # any constraint

class Room(object):
    def __init__(self, bluebox=default_bluebox, greenbox=default_greenbox):
        self.add_something = True # by default
        self.bluebox = bluebox
        self.greenbox = greenbox
        self.add_neighbors = []
        self.remove_neighbors = []

def add_plus(room1, room2):
    pass # XXX implement me
def add_minus(room1, room2):
    pass # XXX implement me
