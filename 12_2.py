from aoc import *

ss = puzzle_input(day=12).strip()
ls = ss.split("\n")
g = to_grid(ss, f=ord)

w, h = len(g[0]), len(g)

from collections import deque

def bfs(g, sources, goal):
    dist = defaultdict(lambda: float("inf"))
    visited = set()

    Q = deque()
    for s in sources:
        visited.add(s)
        dist[s] = 0
        Q.append(s)

    while Q:
        s = Q.popleft()
        for v in g[s]:
            if v not in visited:
                Q.append(v)
                visited.add(v)
                if dist[v] > dist[s] + 1:
                    dist[v] = dist[s] + 1
                if v == goal:
                    return dist[v]

gg = defaultdict(dict)
start, end = ord("S"), ord("E")

for y in range(h):
    for x in range(w):
        if g[y][x] == start:
            start = (x, y)
        elif g[y][x] == end:
            end = (x, y)

g[start[1]][start[0]] = ord("a")
g[end[1]][end[0]] = ord("z")

for y in range(h):
    for x in range(w):
        for dx, dy in dir4(x, y, w, h):
            tgt = g[dy][dx]
            curr = g[y][x]

            if tgt > curr+1:
                continue

            gg[(x, y)][(dx, dy)] = 1

sources = []
for y in range(h):
    for x in range(w):
        if g[y][x] == ord("a"):
            sources.append((x, y))

clipboard(bfs(gg, sources, end))
