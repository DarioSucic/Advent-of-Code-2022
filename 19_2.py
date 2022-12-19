from aoc import *

ss = puzzle_input(day=19).strip()
# Shamelessly stolen from https://github.com/jonathanpaulson/AdventOfCode/blob/master/2022/19.py

from collections import deque
from math import prod

def solve(Co, Cc, Co1, Co2, Cg1, Cg2, t):
    best = 0
    # state is (ore, clay, obsidian, geodes, r1, r2, r3, r4, time)
    Q = deque([(0, 0, 0, 0, 1, 0, 0, 0, t)])
    SEEN = set()
    while Q:
        o, c, ob, g, r1, r2, r3, r4, t = Q.popleft()

        best = max(best, g)
        if t == 0:
            continue

        ore_threshold = max(Co, Cc, Co1, Cg1)
        r1 = min(r1, ore_threshold)
        r2 = min(r2, Co2)
        r3 = min(r3, Cg2)
        o = min(o, t*ore_threshold - r1*(t-1))
        c = min(c, t*Co2 - r2*(t-1))
        ob = min(ob, t*Cg2 - r3*(t-1))

        state = (o, c, ob, g, r1, r2, r3, r4, t)

        if state in SEEN:
            continue

        SEEN.add(state)

        Q.append((o+r1, c+r2, ob+r3, g+r4, r1, r2, r3, r4, t-1))
    
        if r1 != ore_threshold and o >= Co: # buy ore
            Q.append((o-Co+r1, c+r2, ob+r3, g+r4, r1+1, r2, r3, r4, t-1))
        
        if r2 != Co2 and o >= Cc: # buy clay
            Q.append((o-Cc+r1, c+r2, ob+r3, g+r4, r1, r2+1, r3, r4, t-1))

        if r3 != Cg2 and o >= Co1 and c >= Co2: # buy obsidian
            Q.append((o-Co1+r1, c-Co2+r2, ob+r3, g+r4, r1, r2, r3+1, r4, t-1))

        if o >= Cg1 and ob >= Cg2: # buy geode
            Q.append((o-Cg1+r1, c+r2, ob-Cg2+r3, g+r4, r1, r2, r3, r4+1, t-1))

    return best


clipboard(prod(solve(*ints(line)[1:], 32) for i, line in enumerate(ss.split("\n")[:3])))
