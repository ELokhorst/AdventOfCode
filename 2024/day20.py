import heapq
from collections import defaultdict as dd
import math


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


def euclidean_distance(coord1, coord2):
    return math.sqrt((coord2[0] - coord1[0]) ** 2 + (coord2[1] - coord1[1]) ** 2)


def find_cheats(coords):
    coords_set = set(coords)
    cheats = set()

    for x, y in coords:
        if (x + 2, y) in coords_set and (x + 1, y) not in coords_set:
            cheats.add((x + 1, y))
        if (x - 2, y) in coords_set and (x - 1, y) not in coords_set:
            cheats.add((x - 1, y))
        if (x, y + 2) in coords_set and (x, y + 1) not in coords_set:
            cheats.add((x, y + 1))
        if (x, y - 2) in coords_set and (x, y - 1) not in coords_set:
            cheats.add((x, y - 1))

    return cheats


def main(file: str):
    with open(file, "r", encoding="utf-8") as f:
        lines = f.read().strip().splitlines()

    positions = {(x, y): c for y, line in enumerate(lines) for x, c in enumerate(line)}
    coords, start, end = (
        {pos for pos, c in positions.items() if c in "E."},
        next(pos for pos, c in positions.items() if c == "S"),
        next(pos for pos, c in positions.items() if c == "E"),
    )
    normal_cost, parents, costs = find_lowest_cost_paths(coords, start, end)
    print(costs)
    path = backtrack(parents, end)
    pts = find_cheats(path)

    cheat_cost = []
    for pos2add in pts:
        coords.add(pos2add)
        cost, _, _ = find_lowest_cost_paths(coords, start, end)
        cheat_cost.append(normal_cost - cost)
        coords.remove(pos2add)

    print(sum([1 for num in cheat_cost if num >= 100]))
    return cheat_cost


res_example = main("2024/day20_example.txt")
print(res_example)
# res_actual = main("2024/day20_input.txt")
# print(res_actual)
