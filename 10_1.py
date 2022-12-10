from aoc import *

ss = puzzle_input(day=10)
ls = ss.strip().split("\n")

cyc = { 20, 60, 100, 140, 180, 220  }

x = 1
c = 1

global tot
tot = 0

def hook(c, x):
    if c in cyc:
        global tot
        tot += c * x

for l in ls:
    ps = l.split()

    hook(c, x)
    c += 1

    if len(ps) == 2:
        inst, n = ps[0], int(ps[1])
        hook(c, x)
        c += 1
        x += n

clipboard(tot)
