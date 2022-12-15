from aoc import *

ss = puzzle_input(day=15).strip()

def manhattan(a, b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

sensors = []
for l in ss.split("\n"):
    x1, y1, x2, y2 = ints(l)
    d = manhattan((x1, y1), (x2, y2))
    sensors.append(((x1, y1), d))

def border(x, y, d):
    #topleft
    x0, y0 = x-d-1, y
    for _ in range(d+1):
        yield x0, y0
        x0 += 1
        y0 += 1
    
    #topright
    x0, y0 = x, y+d+1
    for _ in range(d+1):
        yield x0, y0
        x0 += 1
        y0 -= 1
    
    #botright
    x0, y0 = x+d+1, y
    for _ in range(d+1):
        yield x0, y0
        x0 -= 1
        y0 -= 1
    
    #botleft
    x0, y0 = x, y-d-1
    for _ in range(d+1):
        yield x0, y0
        x0 -= 1
        y0 += 1


xrng = range(0, 4*10**6+1)
yrng = range(0, 4*10**6+1)

def find_beacon():
    for (x, y), d in sensors:
        for p in border(x, y, d):
            if not (p[0] in xrng and p[1] in yrng):
                continue
            if not any(manhattan(s, p) <= sd for s, sd in sensors):
                return p
                
beacon = find_beacon()
clipboard(beacon[0]*4*10**6 + beacon[1])
