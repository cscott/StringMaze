#!/usr/bin/python

from maze import Room, add_plus, add_minus
from util import *

# 5x5 (25) main rooms, plus one special ENTER and one special EXIT room.

rooms = [
    # room 0 = ENTER node.
    Room(),
    
    # ---- row 1 -----
    # room 1
    Room(root_vegetables, at_least_three_letters_at_least_twice),
    # room 2
    Room(),
    # room 3
    Room(),
    # room 4
    Room(),
    # room 5
    Room(),

    # ---- row 2 -----
    # room 6
    Room(),
    # room 7
    Room(),
    # room 8
    Room(),
    # room 9
    Room(),
    # room 10
    Room(),

    # ---- row 3 -----
    # room 11
    Room(),
    # room 12
    Room(),
    # room 13
    Room(),
    # room 14
    Room(),
    # room 15
    Room(),

    # ---- row 4 -----
    # room 16
    Room(),
    # room 17
    Room(),
    # room 18
    Room(),
    # room 19
    Room(),
    # room 20
    Room(),

    # ---- row 5 -----
    # room 21
    Room(),
    # room 22
    Room(),
    # room 23
    Room(),
    # room 24
    Room(),
    # room 25
    Room(),

    # -- EXIT NODE --
    Room()
    ]
ENTER = rooms[0]
EXIT = rooms[-1]

# the middle room is the only one which doesn't need anything added
rooms[13].add_something = False

# now the +/- connections between them
add_plus(ENTER, rooms[1])
add_plus(rooms[1], rooms[6])
add_plus(rooms[2], rooms[7])
add_plus(rooms[2], rooms[3])
#...

add_minus(rooms[1], rooms[2])
# ...
add_minus(rooms[25], EXIT)
