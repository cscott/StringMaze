#!/usr/bin/python

import mw

default_bluebox = mw.mw_entry
def default_greenbox(s): return False # any constraint

class Room(object):
    def __init__(self, dist, bluebox=None, greenbox=None):
        if bluebox is None: bluebox = default_bluebox
        if greenbox is None: greenbox = default_greenbox
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

def _delete(result, entry):
    if len(entry)==0:
        yield result
        return
    if len(result)==0:
        return
    if result[0]==entry[0]:
        for x in _delete(result[1:], entry[1:]):
            yield x
    for x in _delete(result[1:], entry):
        yield result[0] + x
    return

class State(object):
    def __init__(self, room, result):
        self.room = room # Room object
        self.result = result # string

    def __cmp__(self, other):
        c = cmp(self.room.dist, other.room.dist)
        if c != 0: return c
        return cmp(self.result, other.result)

    def step(self):
        # ok, add entries to the entry nodes
        for neighbor in self.room.add_neighbors:
            for entry in neighbor.bluebox():
                entry = entry.strip().lower()
                if neighbor.add_something:
                    # try prepending
                    nresult = entry + self.result
                    if (len(nresult) < 26) and neighbor.greenbox(nresult):
                        yield State(neighbor, nresult)
                    # try appending
                    nresult = self.result + entry
                    if (len(nresult) < 26) and neighbor.greenbox(nresult):
                        yield State(neighbor, nresult)
                else: # don't add anything (middle box)
                    if neighbor.greenbox(self.result):
                        yield State(neighbor, self.result)
        # do it again, following the 'remove' edges
        for neighbor in self.room.remove_neighbors:
            for entry in neighbor.bluebox():
                entry = entry.strip().lower()
                assert neighbor.add_something
                for nresult in _delete(self.result, entry):
                    if neighbor.greenbox(nresult):
                        yield State(neighbor, nresult)
        # done!
        return
