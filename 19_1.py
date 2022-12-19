from aoc import *

ss = puzzle_input(day=19).strip()

class MaterialMap:
    __slots__ = ["ore", "clay", "obsidian", "geode"]
    def __init__(self, ore, clay, obsidian, geode):
        self.ore: int = ore
        self.clay: int = clay
        self.obsidian: int = obsidian
        self.geode: int = geode

    def __hash__(self):
        return hash((self.ore, self.clay, self.obsidian, self.geode))

    def __repr__(self):
        return f"MaterialMap({self.ore}, {self.clay}, {self.obsidian}, {self.geode})"

    def __getitem__(self, key):
        return getattr(self, key)
    
    def __setitem__(self, key, value):
        return setattr(self, key, value)

    def __add__(self, other):
        return MaterialMap(
            self.ore + other.ore,
            self.clay + other.clay,
            self.obsidian + other.obsidian,
            self.geode + other.geode,
        )

    def __iadd__(self, other):
        self.ore += other.ore
        self.clay += other.clay
        self.obsidian += other.obsidian
        self.geode += other.geode
        return self

    def __sub__(self, other):
        return MaterialMap(
            self.ore - other.ore,
            self.clay - other.clay,
            self.obsidian - other.obsidian,
            self.geode - other.geode,
        )

    def __isub__(self, other):
        self.ore -= other.ore
        self.clay -= other.clay
        self.obsidian -= other.obsidian
        self.geode -= other.geode
        return self

    def copy(self):
        return MaterialMap(self.ore, self.clay, self.obsidian, self.geode)

class State:
    __slots__ = ["robots", "mats"]
    def __init__(self, robots, mats):
        self.robots: MaterialMap = robots
        self.mats: MaterialMap = mats

    def __hash__(self):
        return hash((self.robots, self.mats))

    def __eq__(self, other):
        return self.robots == other.robots and self.mats == other.mat

    def __repr__(self):
        return f"State({self.robots}, {self.mats})"

    def copy(self):
        return State(self.robots.copy(), self.mats.copy())

def can_build(robot_type: str, costs: dict[dict], mat: MaterialMap):
    for material, cost in costs[robot_type].items():
        if mat[material] < cost:
            return False
    return True

def time_to_build(robot_type: str, costs: dict[dict], state: State):
    if can_build(robot_type, costs, state.mats):
        return 0

    time = 0
    for material, cost in costs[robot_type].items():
        if state.robots[material] == 0:
            return 50 # arbitrary large value st. time + wait > 24
        delta = cost - state.mats[material]
        time = max(time, math.ceil(delta / state.robots[material]))
    return time


init_state = State(
    robots=MaterialMap(1, 0, 0, 0),
    mats=MaterialMap(0, 0, 0, 0),
)

total = 0
for l in ss.split("\n"):
    _id, o, c, o1, o2, g1, g2 = ints(l)
    costs = {
        "ore": { "ore": o },
        "clay": { "ore": c },
        "obsidian": { "ore": o1, "clay": o2 },
        "geode": { "ore": g1, "obsidian": g2 },
    }

    ore_max = max(o, c, o1, g1)
    clay_max = o2
    obsidian_max = g2

    thresholds = { "ore": ore_max, "clay": clay_max, "obsidian": obsidian_max}
    
    def should_build(robot_type: str, costs: dict[dict], state: State, built: bool):
        if state.robots[robot_type] > thresholds[robot_type]:
            return False

        if not built:
            prev_mats = state.mats - state.robots
            skipped = can_build(robot_type, costs, prev_mats)
            return not skipped
        
        return True


    from collections import deque

    queue = deque([(init_state.copy(), 0, False)])
    memo = {}

    while queue:
        state, t, built = queue.popleft()
        
        prev_best = memo.get(t, 0)
        if state.mats.geode < prev_best:
            continue
        
        memo[t] = state.mats.geode
        if t == 24:
            continue

        if can_build("geode", costs, state.mats):
            next_state = state.copy()
            next_state.mats += state.robots
            for material, cost in costs["geode"].items():
                next_state.mats[material] -= cost
            next_state.robots.geode += 1
            queue.append((next_state, t + 1, True))
            continue
    
        next_state = state.copy()
        next_state.mats += state.robots
        queue.append((next_state, t + 1, False))
    
        for robot_type in ["obsidian", "clay", "ore"]:
            if not can_build(robot_type, costs, state.mats):
                continue
            if not should_build(robot_type, costs, state, built):
                continue
            next_state = state.copy()
            next_state.mats += state.robots
            for material, cost in costs[robot_type].items():
                next_state.mats[material] -= cost
            next_state.robots[robot_type] += 1
            queue.append((next_state, t + 1, True))

    q = memo[24]
    print(f"{_id=} {q=}")
    total += _id * q

clipboard(total)
