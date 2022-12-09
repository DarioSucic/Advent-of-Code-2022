from aoc import *

ss = puzzle_input(day=9)
ls = ss.strip().split("\n")

rope = [(0, 0) for _ in range(10)]

visited = { (0, 0) }

sign = lambda x: 1 if x > 0 else (-1 if x < 0 else 0)

for l in ls:
    d, n = l.split()
    n = int(n)

    match d:
        case "L": sx, sy = -1, 0
        case "R": sx, sy = 1, 0
        case "D": sx, sy = 0, -1
        case "U": sx, sy = 0, 1
    
    for _ in range(n):
        rope[-1] = (rope[-1][0]+sx, rope[-1][1]+sy)
            
        for t, h in reversed(list(zip(range(9), range(1, 10)))):
            while rope[t] not in dir8(*rope[h]) and rope[t] != rope[h]:
                dx, dy = rope[h][0]-rope[t][0], rope[h][1]-rope[t][1]
                nxt = (rope[t][0] + sign(dx), rope[t][1] + sign(dy))
                if nxt != rope[h]:
                    rope[t] = nxt
                
                if t == 0:
                    visited.add(rope[t])
    
clipboard(len(visited))
