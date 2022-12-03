from aoc import *

ss = puzzle_input(day=3)
ls = ss.strip().split("\n")

def pri(x):
    if x.islower():
        return ord(x)-96
    else:
        return ord(x)-65+27

per_elf = []
for l in ls:
    per_elf.append(set(l))

o=0
for chunk in chunks(per_elf, 3):
    x, y, z = chunk
    cmn = x & y & z
    for v in cmn:
        o += pri(v)

clipboard(o)
