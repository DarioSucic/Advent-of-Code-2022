from aoc import *

lines = read_lines(day=1)
txt = read_string(day=1)

chunks = txt.split("\n\n")
m = 0
for chunk in chunks:
    m = max(m, sum(ints(chunk)))

clipboard(m)
