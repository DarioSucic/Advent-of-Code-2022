from aoc import *

ss = puzzle_input(day=18).strip()

pts = set()
for l in ss.split("\n"):
    x, y, z = ints(l)
    pts.add((x, y, z))

DIRS = [
    (0, 0, 1),
    (-1, 0, 0),
    (1, 0, 0),
    (0, 1, 0),
    (0, -1, 0),
    (0, 0, -1)
]

def nbs(p):
    for d in DIRS:
        yield (p[0] + d[0], p[1] + d[1], p[2] + d[2])

def solve(pts):
    t = 0
    for p in pts:
        for nb in nbs(p):
            if nb not in pts:
                t += 1

    return t


pppts = list(pts)
avg = pppts[0]
for x, y, z in pppts[1:]:
    avg = (avg[0] + x, avg[1] + y, avg[2] + z)
avg = tuple(map(round, (avg[0]/len(pppts), avg[1]/len(pppts), avg[2]/len(pppts))))

def manhattan(a, b):
    return sum(abs(x-y) for x, y in zip(a, b))


xmin = min(x for x, y, z in pts)-2
ymin = min(y for x, y, z in pts)-2
zmin = min(z for x, y, z in pts)-2

xmax = max(x for x, y, z in pts)+2
ymax = max(y for x, y, z in pts)+2
zmax = max(z for x, y, z in pts)+2

def inbounds(p):
    x, y, z = p
    return (xmin <= x <= xmax) and (ymin <= y <= ymax) and (zmin <= z <= zmax)

start = (xmin, ymin, zmin)
outer = { start }
queue = list(nbs(start))
while queue:
    p = queue.pop()
    if p in outer or p in pts or not inbounds(p):
        continue
    outer.add(p)
    queue += nbs(p)


# subtract area of cube walls
top_area = (xmax - xmin + 1) * (ymax - ymin + 1)
side_area = (ymax - ymin + 1) * (zmax - zmin + 1)
front_area = (xmax - xmin + 1) * (zmax - zmin + 1)
cube_walls = 2*top_area + 2*side_area + 2*front_area

clipboard(solve(outer) - cube_walls)
