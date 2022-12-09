from aoc import *

ss = puzzle_input(day=9)
ls = ss.strip().split("\n")

tail = (0, 0)
head = (0, 0)

visited = { tail }

sign = lambda x: (1 if x > 0 else (-1 if x < 0 else 0))

for l in ls:
    d, n = l.split()
    n = int(n)

    match d:
        case "L": head = (head[0]-n, head[1]) 
        case "R": head = (head[0]+n, head[1]) 
        case "D": head = (head[0], head[1]-n) 
        case "U": head = (head[0], head[1]+n)

    while tail not in dir8(*head) and tail != head:
        dx, dy = head[0]-tail[0], head[1]-tail[1]
        tail = (tail[0] + sign(dx), tail[1] + sign(dy))
        visited.add(tail)

clipboard(len(visited))
