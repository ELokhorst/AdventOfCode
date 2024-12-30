from re import findall


def get_shortest_path(grid: dict, start: str, goal: str) -> str:
    sx, sy = grid[start]
    gx, gy = grid[goal]
    _, max_y = max(grid.values())
    dx = gx - sx
    dy = gy - sy

    instr = ""
    if gx == 0 and not gy == 0:
        instr += abs(dy) * "^" if dy < 0 else dy * "v" if dy > 0 else ""
        instr += dx * ">" if dx > 0 else abs(dx) * "<" if dx < 0 else ""
    else:
        instr += abs(dx) * "<" if dx < 0 else dx * ">" if dx > 0 else ""
        instr += abs(dy) * "^" if dy < 0 else dy * "v" if dy > 0 else ""
    instr += "A"
    return instr


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


def walk_path(keypad: dict, path: list[str], start: str):
    next_path = ""
    for p in path:
        shortest = get_shortest_path(keypad, start, p)
        next_path += shortest
        start = p
    return next_path


def main(file: str):
    with open(file, "r", encoding="utf-8") as f:
        numeric_codes = f.read().strip().splitlines()

    nums = [int(n) for line in numeric_codes for n in findall(r"(\d+)", line)]
    keypad_coords = initialize_keypad()
    dirpad_coords = initialize_keypad(dir_kp=True)

    start = "A"
    instructions: dict[str, list] = {}
    for code in numeric_codes:
        path = walk_path(keypad_coords, code, start)

        for _ in range(2):
            path = walk_path(dirpad_coords, path, start)
        instructions[code] = path

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
