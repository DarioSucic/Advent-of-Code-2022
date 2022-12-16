import re, math

from itertools import islice, permutations
from pathlib import Path
from collections import defaultdict, Counter

# --- Parsing -----------------------------------------------------------------

RE_INT   = re.compile(r"-?\d+")
RE_FLOAT = re.compile(r"-?(?:\d?\.\d+|\d+)")

def ints(s: str):
    return list(map(int, RE_INT.findall(s)))

def floats(s: str):
    return list(map(float, RE_FLOAT.findall(s)))

# --- Misc. -------------------------------------------------------------------

def identity(x):
    return x

def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1

def crt(a, n):
    """Chinese Remainder theorem.
        Solves the simultaneous congruence (for x):

        x ≡ aᵢ (mod nᵢ),  i ∈ 1..k

        nᵢ must be pairwise coprime
        0 ≤ aᵢ < nᵢ
    """
    N = math.prod(n)
    total = 0
    for a_i, n_i in zip(a, n):
        p = N // n_i
        total += a_i * mul_inv(p, n_i) * p
    return total % N

def merge_ranges(rs):
    """Merges overlapping `range` objects in the iterable `rs`.

       merge_ranges([range(0, 5), range(2, 7)]) == [range(0, 7)]
    """
    rs = sorted(rs, key = lambda r: r.start)
    out = [rs[0]]
    for r in rs[1:]:
        if r.start in out[-1]:
            if r.stop > out[-1].stop:
                out[-1] = range(out[-1].start, r.stop)
        else:
            out.append(r)

    return out

# --- Iteration / Collections -------------------------------------------------

def chunks(a, k):
    for i in range(0, len(a), k):
        yield a[i:i+k]

def take(it, n):
    return list(islice(it, n))

def nth(it, n):
    return next(islice(it, n, None))

# --- Input / Output -------------------------------------------------------------------

def puzzle_input(day, root_folder=Path(__file__).parent):
    return (root_folder / "inputs" / f"{day}.txt").read_text()

def to_grid(s, f=identity, strip=True):
    if strip:
        return [list(map(f, line.strip())) for line in s.split("\n")]
    else:
        return [list(map(f, line)) for line in s.split("\n")]

def clipboard(x):
    x = str(x).strip()
    print(x)
    return __import__("pyperclip").copy(x)

# --- Spatial -----------------------------------------------------------------

def dir4(x, y, w=None, h=None):
    """W E N S"""
    if w is None or x - 1 >= 0:
        yield x-1, y
    if w is None or x + 1 < w:
        yield x+1, y
    if h is None or y - 1 >= 0:
        yield x, y-1
    if h is None or y + 1 < h:
        yield x, y+1

def corner4(x, y, w=None, h=None):
    """NW NE SW SE"""
    if w is None and h is None or x - 1 >= 0 and y-1 >= 0:
        yield x-1, y-1
    if w is None and h is None or x + 1 < w and y-1 >= 0:
        yield x+1, y-1
    if w is None and h is None or x - 1 >= 0 and y+1 < h:
        yield x-1, y+1
    if w is None and h is None or x + 1 < w and y+1 < h:
        yield x+1, y+1

def dir8(x, y, w=None, h=None):
    """W E N S NW NE SW SE"""
    yield from dir4(x, y, w, h)
    yield from corner4(x, y, w, h)
