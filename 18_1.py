from aoc import *

ss = puzzle_input(day=18).strip()

pts = set()
for l in ss.split("\n"):
    x, y, z = ints(l)
    pts.add((x, y, z))

dirs = [
    (0, 0, 1),
    (-1, 0, 0),
    (1, 0, 0),
    (0, 1, 0),
    (0, -1, 0),
    (0, 0, -1)
]

t = 0
for p in pts:
    for d in dirs:
        nb = (p[0] + d[0], p[1] + d[1], p[2] + d[2])
        if nb in pts:
            continue
        t += 1

clipboard(t)
