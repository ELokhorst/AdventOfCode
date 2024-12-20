import heapq
from collections import defaultdict as dd


def find_lowest_cost_paths(coords: set, start: tuple, end: tuple) -> list:
    directions = [(0, 1), (-1, 0), (0, -1), (1, 0)]
    pq = []
    costs = dd(lambda: float("inf"))
    costs[start] = 0

    heapq.heappush(pq, (0, start))

    while pq:
        cost, current = heapq.heappop(pq)
        cx, cy = current
        if (cx, cy) not in costs:
            costs[(cx, cy)] = 0

        if current == end:
            break

        for dx, dy in directions:
            nx, ny = (cx + dx, cy + dy)

            if (nx, ny) in coords:
                if cost + 1 <= costs[(nx, ny)]:
                    costs[(nx, ny)] = cost + 1
                    heapq.heappush(pq, (costs[(nx, ny)], (nx, ny)))

    return dict(costs)


def manhattan_distance(coord1, coord2):
    return abs(coord2[0] - coord1[0]) + abs(coord2[1] - coord1[1])


def find_cheats(costs: dict):
    coords = set(costs.keys())

    saves = []
    for x, y in coords:
        cheats = set(
            (point, manhattan_distance((x, y), point))
            for point in coords
            if 2 <= manhattan_distance((x, y), point) <= 20
        )
        for cheat, distance in cheats:
            if costs[cheat] > costs[(x, y)]:
                save = costs[cheat] - (costs[(x, y)] + distance)
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
    costs = find_lowest_cost_paths(coords, start, end)
    saves = find_cheats(costs)
    result = sum([1 for num in saves if num >= 100])
    return result


res_example = main("2024/day20_example.txt")
print(res_example)
res_actual = main("2024/day20_input.txt")
print(res_actual)
