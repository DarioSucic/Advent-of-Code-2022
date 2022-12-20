from aoc import *

ss = puzzle_input(day=20).strip()

DEC_KEY = 811589153

def mix(a, xs):
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

    return a


def solve(ss):
    xs = [x * DEC_KEY for x in ints(ss)]

    # assert a == [1, 2, -3, 3, -2, 0, 4]

    seq = [
        [0, -2434767459, 3246356612, -1623178306, 2434767459, 1623178306, 811589153],
        [0, 2434767459, 1623178306, 3246356612, -2434767459, -1623178306, 811589153],
        [0, 811589153, 2434767459, 3246356612, 1623178306, -1623178306, -2434767459],
        [0, 1623178306, -2434767459, 811589153, 2434767459, 3246356612, -1623178306],
        [0, 811589153, -1623178306, 1623178306, -2434767459, 3246356612, 2434767459],
        [0, 811589153, -1623178306, 3246356612, -2434767459, 1623178306, 2434767459],
        [0, -2434767459, 2434767459, 1623178306, -1623178306, 811589153, 3246356612],
        [0, 1623178306, 3246356612, 811589153, -2434767459, 2434767459, -1623178306],
        [0, 811589153, 1623178306, -2434767459, 3246356612, 2434767459, -1623178306],
        [0, -2434767459, 1623178306, 3246356612, -1623178306, 2434767459, 811589153]
    ]

    seen = defaultdict(int)
    a = []
    for x in xs:
        a.append((x, seen[x]))
        seen[x] += 1

    # assert [x for x, _ in a] == [811589153, 1623178306, -2434767459, 2434767459, -1623178306, 0, 3246356612]

    for i in range(10):
        a = mix(a, xs)
        # print([x for x, _ in a])
        # assert ([x for x, _ in a] == seq[i]), f"expected at {i} {seq[i]}"

    assert len(a) == len(xs)

    # k = a.index(0)

    for k, x in enumerate(a):
        if x == (0, 0):
            break

    return a[(k+1000)%len(a)][0] + a[(k+2000)%len(a)][0] + a[(k+3000)%len(a)][0]


clipboard(solve(ss))
