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


ps = [list(map(eval, b.split("\n"))) for b in ss.split("\n\n")]
ps = [p for b in ps for p in b]
ps.append([[2]])
ps.append([[6]])

from functools import cmp_to_key

def cmpkey(l, r):
    c = cmp(l, r)
    if c is True:
        return 1
    if c is False:
        return -1
    return 0

ps.sort(key=cmp_to_key(cmpkey), reverse=True)

ds = []
for i, x in enumerate(ps, 1):
    if x == [[2]] or x == [[6]]:
        ds.append(i)

clipboard(math.prod(ds))
