from aoc import *

ss = puzzle_input(day=6)
ls = ss.strip().split("\n")

for i in range(len(ss)-4):
    chunk = ss[i:i+4]
    if len(set(chunk)) == 4 and i > 2:
        print(i+4)
        break
