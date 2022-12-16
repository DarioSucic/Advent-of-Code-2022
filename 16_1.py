from aoc import *

re_p = r"Valve (\w+) has flow rate=(\d+); tunnels? leads? to valves? (.*)"

ss = puzzle_input(day=16).strip()

from heapq import *

def dijkstra(graph, start, goal):
    dist = {v: float("inf") for v in graph}
    dist[start] = 0

    Q = [(start, dist[start])]
    while Q:
        u, _ = heappop(Q)
        for v in graph[u]:
            alt = dist[u] + graph[u][v]
            if alt < dist[v]:
                dist[v] = alt
                heappush(Q, (v, dist[v]))

    return dist[goal]


mm = {}
for i, l in enumerate(ss.split("\n")):
    m = re.findall(re_p, l)[0]
    v, flow, paths = m
    mm[v] = i

d = defaultdict(dict)
adj = defaultdict(list)
flows = {}
for i, l in enumerate(ss.split("\n")):
    m = re.findall(re_p, l)[0]
    v, flow, paths = m
    
    paths = [p.strip() for p in paths.split(",")]
    for p in paths:
        d[mm[v]][mm[p]] = 1

    adj[mm[v]].extend([mm[p] for p in paths])
    flows[mm[v]] = int(flow)

# import networkx as nx
# graph = nx.from_dict_of_lists(adj)

# print(dijkstra(d, "AA", "CC"))
# nx.draw(graph, with_labels=True)

# import matplotlib.pyplot as plt
# plt.show()

dists = {}
for pos in d:
    dists[pos] = { p: dijkstra(d, pos, p) for p in d if p != pos}

""" Original:
def released(opened):
    return sum(flows[p] for p in opened)

def getkey(opened):
    k2 = 0
    for k in opened:
        k2 |= (1 << k)
    return k2

def solve(pos, t, opened, acc, memo):
    if t == 0:
        return acc
        
    key = hash((acc, pos, t, getkey(opened)))
    if key in memo:
        return memo[key]

    total = released(opened)
    
    choices = []
    if not pos in opened and flows[pos] != 0:
        opened.add(pos)
        v = solve(pos, t-1, opened, acc + total, memo)
        opened.remove(pos)
        choices.append(v)

    # for p in d[pos]:
    #     choices.append(solve(p, t-1, opened, acc + total, memo))

    for p, dist in dists[pos].items():
        if p in opened or dist > t or flows[p] == 0:
            continue
        choices.append(solve(p, t-dist, opened, acc + total*dist, memo))

    if not choices:
        # print("early exit", t)
        return acc + total * t

    ans = max(choices)
    memo[key] = ans
    return ans


pos = mm["AA"]
t = 30
opened = set()

clipboard(solve(pos, t, opened, 0, {}))
"""

def solve(pos, t, fks, memo):
    key = (pos, t, fks)
    if key in memo:
        return memo[key]

    v = 0
    for i, k in enumerate(fks):
        if dists[pos][k] >= t:
            continue

        t_next = t - dists[pos][k] - 1
        v = max(v, flows[k] * t_next + solve(k, t_next, fks[:i] + fks[i+1:], memo))
    
    memo[key] = v
    return v

valid_flow_keys = tuple(k for k, flow in flows.items() if flow > 0)
clipboard(solve(mm["AA"], 30, valid_flow_keys, {}))