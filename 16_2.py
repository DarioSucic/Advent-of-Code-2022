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

def solve2(pos, t, fks, memo):
    try:
        return max(
            flows[k] * (t - dists[pos][k] - 1) + solve2(k, t - dists[pos][k] - 1, fks[:i] + fks[i+1:], memo)
            for i, k in enumerate(fks)
            if dists[pos][k] < t
        )
    except:
        return solve(mm["AA"], 26, fks, memo)

valid_flow_keys = tuple(k for k, flow in flows.items() if flow > 0)
clipboard(solve2(mm["AA"], 26, valid_flow_keys, {}))
