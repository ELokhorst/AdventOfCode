import heapq
from collections import defaultdict as dd


def find_lowest_cost_paths(coords: set, start: tuple, end: tuple) -> list:
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    pq = []
    costs = dd(lambda: float("inf"))
    best_cost = float("inf")

    heapq.heappush(pq, (0, start))

    while pq:
        cost, current = heapq.heappop(pq)

        if current == end and cost <= best_cost:
            print("Best")
            best_cost = cost

        for dx, dy in directions:
            next_pos = (current[0] + dx, current[1] + dy)

            if next_pos in coords:
                if cost + 1 < costs[next_pos]:
                    costs[next_pos] = cost + 1
                    heapq.heappush(pq, (costs[next_pos], next_pos))

    return best_cost


def test_bytes(coords, raw_lines, start, end):
    chunknumber = 2900
    best_cost = 0
    while best_cost < float("inf"):
        best_cost = float("inf")
        lines = raw_lines[:chunknumber]
        print(lines[-2:])

        corrupted = set(tuple(map(int, line.split(","))) for line in lines)
        valid_coords = set(coords) - corrupted
        valid_coords = sorted(valid_coords, key=lambda x: (x[1], x[0]))

        best_cost = find_lowest_cost_paths(valid_coords, start, end)
        chunknumber += 1
    return chunknumber


def main(file: str):
    with open(file, "r", encoding="utf-8") as f:
        lines = f.read().splitlines()

    max_x = 71
    max_y = 71
    coords = [(x, y) for y in range(max_y) for x in range(max_x)]
    start = (0, 0)
    end = (max_x - 1, max_y - 1)

    byte_no = test_bytes(coords, lines, start, end)

    return byte_no


# res_example = main("2024/day18_example.txt")
# print(res_example)
res_actual = main("2024/day18_input.txt")
print(res_actual)
