from aoc import *

ss = puzzle_input(day=4)
ls = ss.strip().split("\n")
o = 0

for l in ls:
    a, b = l.split(",")
    x1, x2 = list(map(int, a.split("-")))
    y1, y2 = list(map(int, b.split("-")))
    
    if (x1 >= y1 and x2 <= y2) or (y1 >= x1 and y2 <= x2):
        o += 1

clipboard(o)
