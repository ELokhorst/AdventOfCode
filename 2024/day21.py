from re import findall
from collections import deque
from itertools import product


def initialize_keypad(dir_kp=False):
    if dir_kp:
        keypad = [[], []]
        keypad[0] = ["X", "^", "A"]
        keypad[1] = ["<", "v", ">"]
    else:
        keypad = [list(range(i, i + 3)) for i in range(7, -3, -3)]
        keypad[3] = ["X", "0", "A"]

    keypad = {
        str(c): (x, y)
        for y, line in enumerate(keypad)
        for x, c in enumerate(line)
        if c != "X"
    }
    return keypad


def get_numeric_path(keypad: dict, path: list[str], start: str):
    paths = []
    for p in path:
        paths.append(all_shortest_paths(keypad, start, p))
        start = p

    combinations = product(*paths)
    paths = ["".join(combo) for combo in combinations]
    min_len = min(map(len, paths))
    shortest_paths = [path for path in paths if len(path) == min_len]
    return shortest_paths


def all_shortest_paths(keypad: dict, start: str, goal: str):
    grid = [val for val in keypad.values()]
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    start = keypad[start]
    goal = keypad[goal]

    visited = {}
    queue = deque([(start, [start])])
    shortest_paths = []
    shortest_length = float("inf")

    while queue:
        (x, y), path = queue.popleft()

        if (x, y) == goal:
            if len(path) < shortest_length:
                shortest_length = len(path)
                shortest_paths = [path]
            elif len(path) == shortest_length:
                shortest_paths.append(path)
            continue

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            next_cell = (nx, ny)

            if next_cell in grid:
                if next_cell not in visited or len(path) + 1 <= shortest_length:
                    queue.append((next_cell, path + [next_cell]))
                    visited[next_cell] = len(path) + 1

    shortest_paths = [press_numeric_keypad(path) for path in shortest_paths]
    return shortest_paths


def press_numeric_keypad(coords):
    directions = {(-1, 0): "<", (1, 0): ">", (0, -1): "^", (0, 1): "v"}
    instr = ""
    for (x1, y1), (x2, y2) in zip(coords, coords[1:]):
        dx, dy = x2 - x1, y2 - y1
        instr += directions.get((dx, 0), "") + directions.get((0, dy), "")
    return instr + "A"


memo_cache = {}


def get_directional_path(keypad: dict, path: list[str], start: str):
    if path in memo_cache:
        return memo_cache[path]

    paths = []
    for p in path:
        paths.append(all_shortest_paths(keypad, start, p))
        start = p

    combinations = product(*paths)
    all_paths = ["".join(combo) for combo in combinations]
    min_len = min(len(path) for path in all_paths)
    shortest_paths = [path for path in all_paths if len(path) == min_len]
    memo_cache[path] = shortest_paths
    return shortest_paths, min_len


def main(file: str):
    with open(file, "r", encoding="utf-8") as f:
        numeric_codes = f.read().strip().splitlines()

    nums = [int(n) for line in numeric_codes for n in findall(r"(\d+)", line)]
    keypad = initialize_keypad()
    dirpad = initialize_keypad(dir_kp=True)

    start = "A"
    instructions: dict[str, list] = {}
    for code in numeric_codes:
        paths = get_numeric_path(keypad, code, start)

        for _ in range(2):
            all_paths = []
            pl = float("inf")
            # print(f"Paths: {paths}")
            for path in paths:
                shortest_paths, path_length = get_directional_path(dirpad, path, start)
                if path_length == pl:
                    all_paths.extend(shortest_paths)
                elif path_length < pl:
                    all_paths = shortest_paths
                    pl = path_length
                else:
                    memo_cache[path] = []
            paths = all_paths
        instructions[code] = min(paths, key=len)

    print(
        [
            (code, len(instruction), instruction)
            for code, instruction in instructions.items()
        ]
    )
    result = sum([len(a) * b for a, b in zip(instructions.values(), nums)])
    return result


res_example = main("2024/day21_example.txt")
print(res_example)
# res_actual = main("2024/day21_input.txt")
# print(res_actual)
