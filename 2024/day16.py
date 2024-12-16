import heapq


def read_layout(lines) -> list:
    coords = [
        (x, y, char)
        for y, line in enumerate(lines)
        for x, char in enumerate(line)
        if char != "#"
    ]
    return coords


def find_lowest_cost_path(coords: set, start: tuple, end: tuple) -> int:
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    pq = []
    heapq.heappush(pq, (0, start, (1, 0)))
    visited = set()

    while pq:
        cost, current, curr_dir = heapq.heappop(pq)

        if current == end:
            return cost

        if (current, curr_dir) in visited:
            continue
        visited.add((current, curr_dir))

        for dx, dy in directions:
            next_pos = (current[0] + dx, current[1] + dy)

            if next_pos in coords:
                next_dir = (dx, dy)
                turn_cost = 1000 if curr_dir != next_dir else 0
                new_cost = cost + 1 + turn_cost
                heapq.heappush(pq, (new_cost, next_pos, next_dir))

    return float("inf")


def main(file: str):
    with open(file, "r", encoding="utf-8") as f:
        lines = f.read().strip().splitlines()

    coords = read_layout(lines)
    start = [(x, y) for x, y, z in coords if z == "S"][0]
    end = [(x, y) for x, y, z in coords if z == "E"][0]
    coords = set((x, y) for x, y, z in coords if z == "." or z == "E")

    best = find_lowest_cost_path(coords, start, end)
    return best


res_example = main("2024/day16_example.txt")
print(res_example)
res_actual = main("2024/day16_input.txt")
print(res_actual)
