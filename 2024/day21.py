from re import findall
from collections import deque


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


def press_keypad(coords):
    instructions = []

    for i in range(len(coords) - 1):
        dx, dy = coords[i + 1][0] - coords[i][0], coords[i + 1][1] - coords[i][1]

        if dx < 0:
            instructions.append("<")
        elif dx > 0:
            instructions.append(">")

        if dy < 0:
            instructions.append("^")
        elif dy > 0:
            instructions.append("v")

    instructions.append("A")
    return "".join(instructions)


def walk_path(
    keypad: dict, path: list[list[str]], start: str, cache: dict, num_pads: int
):
    if num_pads == 0:
        return path

    grid = [keypad[k] for k in keypad]
    next_path = []

    print(f"In: {path}")
    for options in path:
        current_options = []
        for instruction in options:
            if instruction not in cache:
                cache[instruction] = []
                instruction_group = []
                for next_point in instruction:
                    shortest = all_shortest_paths(
                        grid, keypad[start], keypad[next_point]
                    )
                    instruction_group.extend([press_keypad(p) for p in shortest])
                cache[instruction] = instruction_group
            current_options.append(cache[instruction])
        next_path.append(current_options)

    final_path = []
    for group in next_path:
        recursive_result = walk_path(keypad, group, start, cache, num_pads - 1)
        final_path.extend(recursive_result)

    print(f"Out: {final_path}")
    return final_path


def main(file: str):
    with open(file, "r", encoding="utf-8") as f:
        numeric_codes = f.read().strip().splitlines()

    nums = [int(n) for line in numeric_codes for n in findall(r"(\d+)", line)]
    keypad_coords = initialize_keypad()
    dirpad_coords = initialize_keypad(dir_kp=True)

    cache = {}
    start = "A"
    instructions: dict[str, list] = {}
    for code in numeric_codes:
        path = walk_path(keypad_coords, [code], start, cache, 1)

        num_pads = 2
        shortest_path = walk_path(dirpad_coords, path, start, cache, num_pads)
        path = shortest_path

        instructions[code] = path
        break

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
