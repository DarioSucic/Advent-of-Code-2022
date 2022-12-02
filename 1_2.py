from aoc import *

txt = puzzle_input(day=1)

chunks = txt.split("\n\n")
c = Counter()
for i, chunk in enumerate(chunks):
    c[i] = sum(ints(chunk))

clipboard(sum(x[1] for x in c.most_common(3)))
