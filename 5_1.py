from aoc import *

ss = puzzle_input(day=5)
ls = ss.strip().split("\n")

a, b = ss.split("\n\n")
a = a.split("\n")

stacks = []
for i, l in enumerate(a[::-1]):
    for m in re.finditer(r"\[(\w)\]", l):
        idx = m.span()[0]//4
        if len(stacks) < idx+1:
            stacks.extend([] for _ in range(idx+1-len(stacks)))
        stacks[idx].append(m[1])

for l in b.strip().split("\n"):
    n, fr, to = ints(l)
    fr, to = fr-1, to-1
    
    for _ in range(n):
        stacks[to].append(stacks[fr].pop())
    
clipboard("".join(stack[-1] for stack in stacks))
