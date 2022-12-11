from aoc import *

ss = puzzle_input(day=11).strip()

ms = [[] for _ in range(len(ss.split("\n\n")))]
cnts = [0] * len(ms)

for i, b in enumerate(ss.split("\n\n")):
    ls = b.split("\n")
    items = ints(ls[1].split(":")[1])
    ms[i] = items


for r in range(20):
    for i, b in enumerate(ss.split("\n\n")):
        ls = b.split("\n")
        f = eval(f"lambda old: " + ls[2].split(":")[1][7:])
        d = ints(ls[3])[0]
        
        nxt1 = ints(ls[4])[0]
        nxt2 = ints(ls[5])[0]

        items = ms[i]
        ms[i] = []

        for itm in items:
            w = f(itm) // 3
            cnts[i] += 1
            if w % d == 0:
                ms[nxt1].append(w)
            else:
                ms[nxt2].append(w)

xs = sorted(cnts)
clipboard(xs[-1] * xs[-2])
