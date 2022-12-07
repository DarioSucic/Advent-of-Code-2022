from aoc import *

ss = puzzle_input(day=7)
ls = ss.split("\n")

def parse():
    root = {}, []
    node = root

    i = 1
    while i < len(ls):
        l = ls[i]

        if l.startswith("$"):
            _, cmd, *args = l.split(" ")

            if cmd == "ls":
                j = i+1
                while not (ln := ls[j]).startswith("$"):
                    if not ln: return root
                    a, b = ln.split(" ")
                    if a == "dir":
                        node[0][b] = ({}, [])
                    else:
                        node[1].append((b, int(a)))
                    j += 1
                i = j - 1
            elif cmd == "cd":
                dr = args[0]
                if dr == "..":
                    node = node[0][".."]
                else:
                    node[0][dr][0][".."] = node
                    node = node[0][dr]
        i += 1

    return root

def nodesum(node):
    return sum(b for _, b in node[1]) + sum(nodesum(v) for k, v in node[0].items() if k != "..")

def nodes(node):
    def _nodes(node):
        for k, sub in node[0].items():
            if k == "..": continue
            yield sub
            yield from _nodes(sub)
    yield node    
    yield from _nodes(node)

root = parse()

cap = 70000000
target = 30000000
used = nodesum(root)

clipboard(min(ns for node in nodes(root) if (cap - used + (ns := nodesum(node))) >= target))
