from aoc import *

ss = puzzle_input(day=17).strip()

import numpy as np
from itertools import cycle

rocks = iter(cycle([np.array(r, dtype= np.uint8) for r in [
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
]]))

def mapdir(s):
    if s == "<": return np.array([0, -1])
    if s == ">": return np.array([0, +1])
    raise Exception("woops")

from collections import deque

dirs = cycle(map(mapdir, ss))

h = 0

def show(g, hmax=None):
    h = height(g, h)
    if hmax:
        h = min(h, hmax)
    h += 3
    for y in reversed(range(h)):
        print(" ".join("#" if c else "." for c in g[y]))


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
    return (g[y:y+dy, x:x+dx] & piece).any()

def sim(g: np.ndarray, piece: np.ndarray):
    y = height(g, h) + 3
    x = 2

    pos = np.array([y, x])

    if collide(g, piece, pos):
        raise Exception("woops sim")

    while True:
        d = next(dirs)
        nxt_pos = pos + d
        if collide(g, piece, pos + d):
            nxt_pos -= d

        if collide(g, piece, nxt_pos + [-1, 0]):
            put(g, piece, nxt_pos)
            return

        pos = nxt_pos + [-1, 0]
    
g = np.zeros((2022 * 4, 7), dtype=np.uint8)

for _ in range(2022):
    piece = next(rocks)
    sim(g, piece)
    h = height(g, h)

clipboard(height(g))
