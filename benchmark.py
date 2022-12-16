
import os, re, gc, ast
from time import perf_counter_ns
from collections import defaultdict

from tabulate import tabulate

# Import these outside benchmark to avoid skewing result
import numpy

MILLISECOND = 10**6
FILENAME_RE = re.compile(r"(\d+)\_(\d)_?(\w+)?\.py")

class PatchIO(ast.NodeTransformer):
    BLACKLIST = { "print", "clipboard" }
    NOOP_FUNCNAME = "noop"

    def visit_Expr(self, node: ast.Expr):
        if isinstance(node.value, ast.Call) and isinstance(node.value.func, ast.Name):
            if node.value.func.id in self.BLACKLIST:
                node.value.func.id = self.NOOP_FUNCNAME
        return node

def benchmark(filename, n=None):
    with open(filename) as file:
        source = file.read()
    
    root = ast.parse(source, filename)
    PatchIO().visit(root)
    code = compile(root, filename, "exec")

    GLOBALS = { PatchIO.NOOP_FUNCNAME: lambda *args, **kwargs: None }

    # Warmup run / time estimation
    st = perf_counter_ns()
    exec(code, GLOBALS)
    et = perf_counter_ns()

    if n is None:
        target_time = 200*MILLISECOND
        n = min(max(1, target_time // (et - st)), 250)

    measurements = []
    for _ in range(n):
        gc.collect()
        st = perf_counter_ns()
        exec(code, GLOBALS)
        et = perf_counter_ns()
        measurements.append(et-st)

    print(min(measurements), max(measurements))

    return measurements

if __name__ == "__main__":

    import sys

    args = sys.argv
    if len(args) >= 2:
        path = args[1]
        n = int(args[2]) if len(args) > 2 else None
        measurements = benchmark(path, n)
        print(f"{path} :: {min(measurements)//10**3:>10,} µs")
        exit(0)

    paths = []
    for path in os.listdir("."):
        if (match := FILENAME_RE.match(path)):
            day, part, extra = match.groups()
            day, part = map(int, (day, part))
            paths.append((day, part, bool(extra), path))
    paths.sort()

    results = defaultdict(dict)
    for day, part, extra, path in paths:
        print(path, flush=False, end="\t")
        measurements = benchmark(path)
        time_str = f"{min(measurements)//10**3:>12,} µs"
        results[day][part + int(extra)] = time_str
        print(results[day][part + int(extra)])
        # print(f"Puzzle {day:2}.{part} {min(measurements)//10**3:>16,} µs")

    table = [(day, *parts.values()) for day, parts in results.items()]
    print(tabulate(table, headers=("Day", "Part 1", "Part 2", "Extra"), tablefmt="github"))