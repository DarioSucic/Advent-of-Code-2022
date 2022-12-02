from aoc import *

ss = puzzle_input(day=2)

m={"A":1,"B":2,"C":3,"X":1,"Y":2,"Z":3}

o=0
for line in ss.strip().split("\n"):
    a, b = line.split()
    a, b = m[a], m[b]
    
    if a == b:
        score=3
    elif (b+1)%3+1 == a:
        score=6
    else:
        score=0

    o+=score+b

clipboard(o)
