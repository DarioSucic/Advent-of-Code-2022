from aoc import *

ss = puzzle_input(day=8)
ls = ss.split("\n")

g = read_grid(day=8, f=int)[:-1]

w, h = len(g[0]), len(g)

def isvis(g, i, j):
    t = g[i][j]
    for dy, dx in dir4(0, 0):
        sy, sx = i, j
        found = True
        while True:
            sy, sx = sy+dy, sx+dx
            if not ((0 <= sx < w) and (0 <= sy < h)):
                break

            if g[sy][sx] >= t:
                found = False
                break

        if found: return True

    return False

o = 2*w + 2*h - 4
for i in range(1, len(g)-1):
    for j in range(1, len(g[0])-1):
        o += isvis(g, i, j)

clipboard(o)
