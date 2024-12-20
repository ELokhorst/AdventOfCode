import heapq
from collections import defaultdict as dd


def find_lowest_cost_paths(coords: set, start: tuple, end: tuple) -> list:
    directions = [(0, 1), (-1, 0), (0, -1), (1, 0)]
    pq = []
    costs = dd(lambda: float("inf"))
    parents = dd(set)
    best_cost = float("inf")

    heapq.heappush(pq, (0, start))

    while pq:
        cost, current = heapq.heappop(pq)
        cx, cy = current
        if (cx, cy) not in costs:
            costs[(cx, cy)] = 0

        if current == end and cost <= best_cost:
            best_cost = cost

        for dx, dy in directions:
            nx, ny = (cx + dx, cy + dy)

            if (nx, ny) in coords:
                if cost + 1 <= costs[(nx, ny)]:
                    costs[(nx, ny)] = cost + 1
                    heapq.heappush(pq, (costs[(nx, ny)], (nx, ny)))
                    parents[(nx, ny)] = {current}
                elif cost + 1 == costs[(nx, ny)]:
                    parents[(nx, ny)].add(current)

    return best_cost, parents, costs


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


def manhattan_distance(coord1, coord2):
    return abs(coord2[0] - coord1[0]) + abs(coord2[1] - coord1[1])


def find_cheats(costs: dict):
    coords = set(costs.keys())

    saves = []
    for x, y in coords:
        normal_cost = costs[(x, y)]
        cheats = set(
            (point, manhattan_distance((x, y), point))
            for point in coords
            if manhattan_distance((x, y), point) == 2
        )
        for cheat, distance in cheats:
            cheat_cost = costs[cheat]
            if cheat_cost > normal_cost:
                save = cheat_cost - (normal_cost + distance)
                if save > 0:
                    saves.append(save)

    return saves


def main(file: str):
    with open(file, "r", encoding="utf-8") as f:
        lines = f.read().strip().splitlines()

    positions = {(x, y): c for y, line in enumerate(lines) for x, c in enumerate(line)}
    coords, start, end = (
        {pos for pos, c in positions.items() if c in "E."},
        next(pos for pos, c in positions.items() if c == "S"),
        next(pos for pos, c in positions.items() if c == "E"),
    )
    _, _, costs = find_lowest_cost_paths(coords, start, end)
    costs = dict(costs)
    saves = find_cheats(costs)

    print(sum([1 for num in saves if num >= 100]))
    return saves


res_example = main("2024/day20_example.txt")
print(res_example)
res_actual = main("2024/day20_input.txt")
print(res_actual)
