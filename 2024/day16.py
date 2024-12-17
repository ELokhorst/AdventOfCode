import heapq
from collections import defaultdict as dd


def read_layout(lines) -> list:
    coords = [
        (x, y, char)
        for y, line in enumerate(lines)
        for x, char in enumerate(line)
        if char != "#"
    ]
    return coords


def get_adj_coords(coords, current):
    directions = [(0, 1), (-1, 0), (0, -1), (1, 0)]
    cx, cy, current_dir = current

    yield 1000, (cx, cy, (current_dir - 1) % 4)
    yield 1000, (cx, cy, (current_dir + 1) % 4)
    dx, dy = directions[current_dir]
    nx, ny = (current[0] + dx, current[1] + dy)
    if (nx, ny) in coords:
        yield 1, (nx, ny, current_dir)


def find_lowest_cost_paths(coords: set, start: tuple, end: tuple) -> list:
    pq = []
    costs = dd(lambda: float("inf"))
    from_ = dd(set)
    best_cost = float("inf")

    heapq.heappush(pq, (0, start))

    while pq:
        cost, current = heapq.heappop(pq)
        cx, cy = current[:2]
        ex, ey = end[:2]

        if (cx, cy) == (ex, ey) and cost <= best_cost:
            best_cost = cost

        for added_cost, adj in get_adj_coords(coords, current):
            if cost + added_cost < costs[adj]:
                costs[adj] = cost + added_cost
                heapq.heappush(pq, (costs[adj], adj))
                from_[adj] = {current}
            elif cost + added_cost == costs[adj]:
                from_[adj].add(current)

    return best_cost, from_


def backtrack(parents, end: tuple):
    stack = [end]
    visited = set(stack)
    while stack:
        node = stack.pop(-1)
        for parent in parents[node]:
            if parent not in visited:
                visited.add(parent)
                stack.append(parent)
    return visited


def main(file: str):
    with open(file, "r", encoding="utf-8") as f:
        lines = f.read().strip().splitlines()

    coords = read_layout(lines)
    sx, sy = [(x, y) for x, y, z in coords if z == "S"][0]
    start = (sx, sy, 3)
    ex, ey = [(x, y) for x, y, z in coords if z == "E"][0]
    end = (ex, ey, 1)
    coords = set((x, y) for x, y, z in coords if z == "." or z == "E")

    best, parents = find_lowest_cost_paths(coords, start, end)
    print(best)
    visited = backtrack(parents, end)
    unq = len(set(node[:2] for node in visited))
    return unq


res_example = main("2024/day16_example.txt")
print(res_example)
res_actual = main("2024/day16_input.txt")
print(res_actual)
