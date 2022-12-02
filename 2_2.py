from aoc import *

ss = puzzle_input(day=2)

m={"A":1,"B":2,"C":3,"X":1,"Y":2,"Z":3}

o=0
for line in ss.strip().split("\n"):
    a, b = line.split()
    a, b = m[a], m[b]

    if b == 1:
        score=0
        b = (a-1-1)%3+1
    elif b == 2:
        score=3
        b = a
    else:
        score=6
        b = (a-1+1)%3+1

    o+=score+b


clipboard(o)
