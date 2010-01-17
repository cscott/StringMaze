#!/usr/bin/python

from maze import Room, add_plus, add_minus
from util import *

# 5x5 (25) main rooms, plus one special ENTER and one special EXIT room.

rooms = [
    # room 0 = ENTER node.
    Room(10),
    
    # ---- row 1 -----
    # room 1
    Room(9, root_vegetables, at_least_three_letters_at_least_twice),
    # room 2
    Room(8),
    # room 3
    Room(7),
    # room 4
    Room(6),
    # room 5
    Room(5),

    # ---- row 2 -----
    # room 6
    Room(8),
    # room 7
    Room(7),
    # room 8
    Room(6),
    # room 9
    Room(5),
    # room 10
    Room(4),

    # ---- row 3 -----
    # room 11
    Room(7),
    # room 12
    Room(6),
    # room 13
    Room(5),
    # room 14
    Room(4),
    # room 15
    Room(3),

    # ---- row 4 -----
    # room 16
    Room(6),
    # room 17
    Room(5),
    # room 18
    Room(4),
    # room 19
    Room(3),
    # room 20
    Room(2),

    # ---- row 5 -----
    # room 21
    Room(5),
    # room 22
    Room(4),
    # room 23
    Room(3),
    # room 24
    Room(2),
    # room 25
    Room(1),

    # -- EXIT NODE --
    Room(0)
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
add_plus(rooms[3], rooms[4])
add_plus(rooms[4], rooms[9])
add_plus(rooms[5], rooms[10])
add_plus(rooms[6], rooms[7])
add_plus(rooms[8], rooms[9])
add_plus(rooms[8], rooms[13])
add_plus(rooms[10], rooms[15])
add_plus(rooms[11], rooms[12])
add_plus(rooms[11], rooms[16])
add_plus(rooms[12], rooms[13])
add_plus(rooms[12], rooms[17])
add_plus(rooms[13], rooms[14])
add_plus(rooms[13], rooms[18])
add_plus(rooms[14], rooms[15])
add_plus(rooms[17], rooms[18])
add_plus(rooms[17], rooms[22])
add_plus(rooms[18], rooms[19])
add_plus(rooms[18], rooms[23])
add_plus(rooms[19], rooms[20])
add_plus(rooms[21], rooms[22])
add_plus(rooms[23], rooms[24])

add_minus(rooms[1], rooms[2])
add_minus(rooms[3], rooms[8])
add_minus(rooms[4], rooms[5])
add_minus(rooms[6], rooms[11])
add_minus(rooms[7], rooms[8])
add_minus(rooms[7], rooms[12])
add_minus(rooms[9], rooms[10])
add_minus(rooms[9], rooms[14])
add_minus(rooms[14], rooms[19])
add_minus(rooms[15], rooms[20])
add_minus(rooms[16], rooms[17])
add_minus(rooms[16], rooms[21])
add_minus(rooms[19], rooms[24])
add_minus(rooms[20], rooms[25])
add_minus(rooms[22], rooms[23])
add_minus(rooms[24], rooms[25])
add_minus(rooms[25], EXIT)
