from aoc import *

ss = puzzle_input(day=3)
ls = ss.split("\n")

def pri(x):
    if x.islower():
        return ord(x)-96
    else:
        return ord(x)-65+27

o=0
for l in ls:
    a, b = l[:len(l)//2], l[len(l)//2:]
    eq = set(a) & set(b)
    s = 0
    for x in eq:
        s += pri(x)
    o+=s

clipboard(o)
