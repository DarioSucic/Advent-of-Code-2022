from aoc import *

ss = puzzle_input(day=21).strip()

# Math operators
p = re.compile(r"(\+|\*|\/|\-)")

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

    v = eval(f"lambda {','.join(args[::2])}: {b}")(*arg_vals)
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

    return int(dive("root", nums, evals))
    

clipboard(solve(ss))
