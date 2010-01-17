#!/usr/bin/python

def mw_entry():
    yield "codex" # XXX implement generator for M-W entries.

default_bluebox = mw_entry
def default_greenbox(s): return False # any constraint

class Room(object):
    def __init__(self, dist,
                 bluebox=default_bluebox, greenbox=default_greenbox):
        self.dist = dist
        self.add_something = True # by default
        self.bluebox = bluebox
        self.greenbox = greenbox
        self.add_neighbors = []
        self.remove_neighbors = []

def add_plus(room1, room2):
    room1.add_neighbors.append(room2)
    room2.add_neighbors.append(room1)

def add_minus(room1, room2):
    room1.remove_neighbors.append(room2)
    room2.remove_neighbors.append(room1)

class State(object):
    def __init__(self, room, result):
        self.room = room # Room object
        self.result = result # string

    def __cmp__(self, other):
        c = cmp(self.room.dist, other.room.dist)
        if c != 0: return c
        return cmp(self.room.result, other.room.result)

    def step(self):
        # ok, add entries to the entry nodes
        for neighbor in self.room.add_neighbors:
            for entry in neighbor.bluebox():
                if neighbor.add_something:
                    # try prepending
                    nresult = entry + self.result
                    if neighbor.greenbox(nresult):
                        yield State(neighbor, nresult)
                    # try appending
                    nresult = self.result + entry
                    if neighbor.greenbox(nresult):
                        yield State(neighbor, nresult)
                else: # don't add anything (middle box)
                    if neighbor.greenbox(self.result):
                        yield State(neighbor, self.result)
        # do it again, following the 'remove' edges
        for neighbor in self.room.remove_neighbors:
            for entry in neighbor.bluebox():
                assert neighbor.add_something
                for nresult in delete(result, entry):
                    if neighbor.greenbox(nresult):
                        yield State(neighbor, nresult)
        # done!
        return
