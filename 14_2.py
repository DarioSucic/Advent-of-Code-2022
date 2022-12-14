from aoc import *

ss = puzzle_input(day=14).strip()

paths = []
for l in ss.split("\n"):
    paths.append([ints(p) for p in l.split(" -> ")])

s = (500, 0)
g = defaultdict(bool)
for p in paths:
    for ((x1, y1), (x2, y2)) in zip(p, p[1:]):
        if y1 == y2:
            for x in range(min(x1, x2), max(x1, x2)+1):
                g[(x, y1)] = True
        else:
            for y in range(min(y1, y2), max(y1, y2)+1):
                g[(x1, y)] = True

            
xmin, xmax = min(x for x, y in g.keys())-1000, max(x for x, y in g.keys()) + 1000

lowest = max(y for x, y in g.keys())
floor = lowest + 2
for x in range(xmin, xmax):
    g[(x, floor)] = True

def fall():
    x, y = s
    while y <= floor:
        if not g[(x, y+1)]:
            y += 1
            continue
        
        if not g[(x-1, y+1)]:
            x -= 1
            y += 1
            continue
    
        if not g[(x+1, y+1)]:
            x += 1
            y += 1
            continue

        g[(x, y)] = True
        if (x, y) == s:
            return True
        return False
    
    return False

rest = 1
while not fall():
    rest += 1

clipboard(rest)
