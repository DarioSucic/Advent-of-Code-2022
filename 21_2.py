from aoc import *

ss = puzzle_input(day=21).strip()

# Math operators
p = re.compile(r"(\+|\*|\/|\-)")

import sympy

def dive(key, nums, evals):
    if key in nums:
        return nums[key]
    
    b = evals[key]
    args = list(map(str.strip, p.split(b)))
    arg_vals = []
    for arg in args[::2]:
        try:
            arg_vals.append(int(arg))
        except:
            arg_vals.append(dive(arg, nums, evals))

    if key == "root":
        b = f"({b.replace('+', ',')})"

    f = eval(f"lambda {','.join(args[::2])}: {b}")

    v = f(*arg_vals)
    nums[v] = v
    return v


def solve(ss):
    nums = {}
    evals = {}
    ls = ss.split("\n")
    for l in ls:
        a, b = l.split(": ")
        try:
            x = int(b)
            nums[a] = x
            continue
        except:
            pass

        evals[a] = b

    humn = sympy.symbols("humn")
    nums["humn"] = humn
    a, b = dive("root", nums, evals)

    # solve a == b
    return sympy.solve(a - b, humn)[0].round()

clipboard(solve(ss))
