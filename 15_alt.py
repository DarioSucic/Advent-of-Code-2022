from aoc import *

ss = puzzle_input(day=15).strip()

# -- Part 1 --

def manhattan(a, b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

ds = {}
sensors = {}
for x1, y1, x2, y2 in map(ints, ss.split("\n")):
    sensors[(x1, y1)] = (x2, y2)
    ds[(x1, y1)] = manhattan((x1, y1), (x2, y2))

rs = []
for sx, sy in sensors:
    d = ds[(sx, sy)]
    dy = abs(2000000 - sy)
    if dy <= d:
        rs.append(range(sx-(d-dy), sx+(d-dy)+1))

t = sum(r.stop - r.start for r in merge_ranges(rs))
t -= sum(beacon[1] == 2000000 for beacon in set(sensors.values()))
print("Part 1:", t)

# -- Part 2 --

import z3

solver = z3.Solver()
x, y = z3.Ints("x y")

solver.add(0 <= x, x <= 4_000_000, 0 <= y, y <= 4_000_000)
for sx, sy in sensors:
    solver.add(z3.Abs(x - sx) + z3.Abs(y - sy) > ds[(sx, sy)])

solver.check()
model = solver.model()
print("Part 2:", model[x].as_long() * 4_000_000 + model[y].as_long())
