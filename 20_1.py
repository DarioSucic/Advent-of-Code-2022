from aoc import *

ss = puzzle_input(day=20).strip()

def solve(ss):
    xs = ints(ss)

    # assert a == [1, 2, -3, 3, -2, 0, 4]

    seq = [
        [2, 1, -3, 3, -2, 0, 4],
        [1, -3, 2, 3, -2, 0, 4],
        [1, 2, 3, -2, -3, 0, 4],
        [1, 2, -2, -3, 0, 3, 4],
        [1, 2, -3, 0, 3, 4, -2],
        [1, 2, -3, 0, 3, 4, -2],
        [1, 2, -3, 4, 0, 3, -2]
    ]


    mm = defaultdict(set)

    seen = defaultdict(int)
    a = []
    for x in xs:
        a.append((x, seen[x]))
        seen[x] += 1

    counts = defaultdict(int)

    for i, x in enumerate(xs):
        
        n = counts[x]
        for j, y in enumerate(a):
            if y == (x, n):
                counts[x] += 1
                break

        new_pos = (j + x) % (len(xs)-1)
        if new_pos == j:
            continue

        x = a.pop(j)

        # print(f"a without {x}: {a}")

        # if j + x < 0:
        #     a.insert(new_pos-1, x)
        # else:
        #     if new_pos == 0:
        #         a.append(x)
        #     elif new_pos == len(xs):
        #         a.insert(new_pos, x)
        if new_pos == 0:
            a.append(x)
        else:
            a.insert(new_pos, x)


        # print(f"{x} at position {j} wants to move to {new_pos}")
        # print(a)
        # assert a == seq[i], f"expected {seq[i]}"
        # assert [x[0] for x in a] == seq[i]


    assert len(a) == len(xs)

    # k = a.index(0)

    for k, x in enumerate(a):
        if x == (0, 0):
            break

    return a[(k+1000)%len(a)][0] + a[(k+2000)%len(a)][0] + a[(k+3000)%len(a)][0]


clipboard(solve(ss))
