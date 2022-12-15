from aoc import *

ss = puzzle_input(day=15).strip()

def manhattan(a, b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

ds = {}
sensors = {}
for l in ss.split("\n"):
    x1, y1, x2, y2 = ints(l)
    sensors[(x1, y1)] = (x2, y2)
    d = manhattan((x1, y1), (x2, y2))
    ds[(x1, y1)] = d


""" Original slow version:
xmin, xmax = min(x for x, y in sensors), max(x for x, y in sensors)

s1 = min(sensors, key = lambda p: p[0])
s2 = max(sensors, key = lambda p: p[0])

xmin = s1[0] - manhattan(s1, sensors[s1])
xmax = s2[0] + manhattan(s2, sensors[s2])

y = 2000000
t = 0
for x in range(xmin, xmax):
    if (x, y) in sensors.values():
        continue
    for s in sensors:
        if manhattan(s, (x, y)) <= ds[s]:
            t += 1
            break

clipboard(t)
"""

y = 2000000

rs = []
for sx, sy in sensors:
    d = ds[(sx, sy)]
    dy = abs(y - sy)
    if dy <= d:
        rs.append(range(sx-(d-dy), sx+(d-dy)+1))

t = 0
for r in merge_ranges(rs):
    t += r.stop - r.start

for beacon in set(sensors.values()):
    if beacon[1] == y:
        t -= 1

clipboard(t)