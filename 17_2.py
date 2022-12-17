from aoc import *

ss = puzzle_input(day=17).strip()

import numpy as np
from itertools import cycle

rock_idx = 0
rocks = [np.array(r, dtype= np.uint8) for r in [
    [
        [1, 1, 1, 1]
    ],

    [
        [0, 1, 0],
        [1, 1, 1],
        [0, 1, 0]
    ],

    [
        [0, 0, 1],
        [0, 0, 1],
        [1, 1, 1]
    ][::-1],

    [
        [1],
        [1],
        [1],
        [1]
    ],

    [
        [1, 1],
        [1, 1]
    ]
]]

def mapdir(s):
    if s == "<": return np.array([0, -1])
    if s == ">": return np.array([0, +1])
    raise Exception("woops")

from collections import deque

dir_idx = 0
dirs = list(map(mapdir, ss))

h = 0

def put(g, piece, pos):
    y, x = pos
    dy, dx = piece.shape
    g[y:y+dy, x:x+dx] += piece

def height(g, prev=0):
    for y in range(prev, len(g)):
        if not g[y].any():
            return y

def collide(g, piece, pos):
    y, x = pos
    dy, dx = piece.shape
    if x < 0: return True
    if x+dx-1 > g.shape[1]-1: return True
    if y < 0: return True
    ret = (g[y:y+dy, x:x+dx] & piece).any()
    return ret

def sim(g: np.ndarray, piece: np.ndarray):
    y = height(g, h) + 3
    x = 2

    pos = np.array([y, x])

    global dir_idx

    while True:
        d = dirs[dir_idx]
        dir_idx = (dir_idx + 1) % len(dirs)

        nxt_pos = pos + d
        if collide(g, piece, pos + d):
            nxt_pos -= d

        if collide(g, piece, nxt_pos + [-1, 0]):
            put(g, piece, nxt_pos)
            return

        pos = nxt_pos + [-1, 0]
    
g = np.zeros((20_000, 7), dtype=np.uint8)

d1, d2 = 5, len(ss)

history = defaultdict(list)
hsize = 25

i = 1
while True:
    piece = rocks[rock_idx]
    rock_idx = (rock_idx + 1) % len(rocks)
    sim(g, piece)

    h = height(g, h)

    key = (dir_idx, rock_idx, g[h-hsize:h].tobytes())
    history[key].append((i, h))

    if len(history[key]) == 2:
        (ai, ah), (bi, bh) = history[key]
        di = bi - ai
        dh = bh - ah
        break

    i += 1


n_jumps, rem = divmod(1000000000000 - i, di)

h0 = h
for _ in range(rem):
    piece = rocks[rock_idx]
    rock_idx = (rock_idx + 1) % len(rocks)
    sim(g, piece)
    h = height(g, h)

clipboard(h0 + (n_jumps * dh) + (h - h0))
