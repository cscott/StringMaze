#!/usr/bin/python

import maze, layout
import heapq

def main():
    # simple enough
    initial_state = maze.State(layout.ENTER, "ENTER")
    states = []
    heapq.heappush(states, initial_state)
    while states:
        state = heapq.heappop(states)
        print len(states), "states; best distance:", state.room.dist
        if state.room is layout.EXIT:
            print "SOLUTION:", state.result
            continue
        # otherwise, keep searching
        for nstate in state.step():
            heapq.heappush(states, nstate)

main()
