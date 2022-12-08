from aoc import *

ss = puzzle_input(day=8)
ls = ss.split("\n")

g = read_grid(day=8, f=int)[:-1]

w, h = len(g[0]), len(g)

def score(g, i, j):
    t = g[i][j]
    m = 1
    for dy, dx in dir4(0, 0):
        sy, sx = i, j
        c = 0
        while True:
            sy, sx = sy+dy, sx+dx
            if not ((0 <= sx < w) and (0 <= sy < h)):
                break

            c += 1
            if g[sy][sx] >= t:
                break

        m *= c

    return m

o = 0
for i in range(1, len(g)-1):
    for j in range(1, len(g[0])-1):
        o = max(o, score(g, i, j))

clipboard(o)
