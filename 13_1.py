from aoc import *

from heapq import heapify, heappush, heappop

ss = puzzle_input(day=13).strip()

def cmp(l, r):
    if isinstance(l, int) and isinstance(r, int):
        if l < r:
            return True
        elif l > r:
            return False
        else:
            return None

    elif isinstance(l, list) and isinstance(r, list):
        nl, nr = len(l), len(r)

        for i in range(max(nl, nr)):
            if i > nl-1 and nl != nr:
                return True
            if i > nr-1 and nl != nr:
                return False

            c = cmp(l[i], r[i])
            if c is True:
                return True
            if c is False:
                return False

        return None
                    
    elif isinstance(l, list):
        return cmp(l, [r])
    else:
        return cmp([l], r)


ps = ss.split("\n\n")

t = 0
for i, b in enumerate(ps, 1):
    x, y = map(eval, b.split("\n"))
    if cmp(x, y):
        t += i

clipboard(t)
