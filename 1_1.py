from aoc import *

txt = puzzle_input(day=1)

chunks = txt.split("\n\n")
m = 0
for chunk in chunks:
    m = max(m, sum(ints(chunk)))

clipboard(m)
