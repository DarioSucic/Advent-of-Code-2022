from aoc import *

ss = puzzle_input(day=6)
ls = ss.strip().split("\n")

for i in range(len(ss)-14):
    chunk = ss[i:i+14]
    if len(set(chunk)) == 14 and i > 2:
        print(i+14)
        break
