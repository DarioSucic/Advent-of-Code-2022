from aoc import *

from heapq import heapify, heappush, heappop

ss = puzzle_input(day=12).strip()
ls = ss.split("\n")
g = to_grid(ss, f=ord)

w, h = len(g[0]), len(g)

def dijkstra(graph, start, goal):
    dist = {v: float("inf") for v in graph}
    dist[start] = 0
    prev = {}

    Q = [(start, dist[start])]
    while Q:
        u, _ = heappop(Q)

        for v in graph[u]:
            alt = dist[u] + graph[u][v]
            if alt < dist[v]:
                dist[v] = alt
                prev[v] = u
                heappush(Q, (v, dist[v]))

    return dist[goal]

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
        gg[(x, y)]
        for dx, dy in dir4(x, y, w, h):
            tgt = g[dy][dx]
            curr = g[y][x]

            if tgt > curr+1:
                continue

            gg[(x, y)][(dx, dy)] = 1

clipboard(dijkstra(gg, start, end))
