from re import findall
from collections import deque
from itertools import product


def all_shortest_paths(grid, start, goal):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
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

    return shortest_paths


def initialize_keypad(dir_kp=False):
    if dir_kp:
        keypad = [[], []]
        keypad[0] = ["X", "^", "A"]
        keypad[1] = ["<", "v", ">"]
    else:
        keypad = [list(range(i, i + 3)) for i in range(7, -3, -3)]
        keypad[3] = ["X", "0", "A"]

    keypad = {
        str(c): (x, y) for y, line in enumerate(keypad) for x, c in enumerate(line)
    }
    keypad.pop("X")
    return keypad


def press_numeric_keypad(coords):
    instr = ""
    for i in range(len(coords) - 1):
        dx, dy = coords[i + 1][0] - coords[i][0], coords[i + 1][1] - coords[i][1]
        instr += "<" if dx < 0 else ">" if dx > 0 else ""
        instr += "^" if dy < 0 else "v" if dy > 0 else ""
    instr += "A"
    return instr


def walk_path(keypad: dict, path: list[str], start: str):
    grid = [val for val in keypad.values()]
    paths = []
    for p in path:
        shortest = all_shortest_paths(grid, keypad[start], keypad[p])
        paths.append([press_numeric_keypad(path) for path in shortest])
        start = p

    combinations = product(*paths)
    paths = ["".join(combo) for combo in combinations]
    min_len = min(map(len, paths))
    shortest_paths = [path for path in paths if len(path) == min_len]
    return shortest_paths


def main(file: str):
    with open(file, "r", encoding="utf-8") as f:
        numeric_codes = f.read().strip().splitlines()

    nums = [int(n) for line in numeric_codes for n in findall(r"(\d+)", line)]
    keypad_coords = initialize_keypad()
    dirpad_coords = initialize_keypad(dir_kp=True)

    start = "A"
    instructions: dict[str, list] = {}
    for code in numeric_codes:
        paths = walk_path(keypad_coords, code, start)

        for _ in range(2):
            next_paths = []
            for path in paths:
                next_paths.extend(walk_path(dirpad_coords, path, start))
            paths = next_paths
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
res_actual = main("2024/day21_input.txt")
print(res_actual)
