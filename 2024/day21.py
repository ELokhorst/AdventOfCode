from re import findall


def initialize_keypad(dir_kp=False):
    if dir_kp:
        keypad = [[], []]
        keypad[0] = ["X", "^", "A"]
        keypad[1] = ["<", "v", ">"]
    else:
        keypad = [list(range(i, i + 3)) for i in range(7, -3, -3)]
        keypad[3][0] = "X"
        keypad[3][2] = "A"
        keypad[3][1] = 0
    return {str(c): (x, y) for y, line in enumerate(keypad) for x, c in enumerate(line)}


def press_numeric_keypad(dx, dy):
    instr = ""
    instr += "^" * abs(dy) if dy < 0 else "v" * dy
    if dx > 0:
        instr += ">" * dx
    if dx < 0:
        instr += "<" * abs(dx)
    instr += "A"
    return instr


def press_directional_keypad(dx, dy):
    instr = ""
    if dx > 0:
        instr += ">" * dx
    if dy < 0:
        instr += "^" * abs(dy)
    if dx < 0:
        instr += "<" * abs(dx)
    if dy > 0:
        instr += "v" * dy

    instr += "A"
    return instr


def main(file: str):
    with open(file, "r", encoding="utf-8") as f:
        numeric_codes = f.read().strip().splitlines()

    nums = [int(n) for line in numeric_codes for n in findall(r"(\d+)", line)]

    keypad_coords = initialize_keypad()
    cx, cy = keypad_coords["A"]
    instructions = []
    for code in numeric_codes:
        instruction = ""
        for p in code:
            nx, ny = keypad_coords[p]
            dx, dy = nx - cx, ny - cy
            instruction += press_numeric_keypad(dx, dy)
            cx, cy = nx, ny
        instructions.append(instruction)
    print(instructions[-1])

    keypad_coords = initialize_keypad(dir_kp=True)
    cx, cy = keypad_coords["A"]
    instructions2 = []
    for code in instructions:
        instruction = ""
        for p in code:
            nx, ny = keypad_coords[p]
            dx, dy = nx - cx, ny - cy
            instruction += press_directional_keypad(dx, dy)
            cx, cy = nx, ny
        instructions2.append(instruction)
    print(instructions2[-1])

    keypad_coords = initialize_keypad(dir_kp=True)
    cx, cy = keypad_coords["A"]
    instructions3 = []
    for code in instructions2:
        instruction = ""
        for p in code:
            nx, ny = keypad_coords[p]
            dx, dy = nx - cx, ny - cy
            instruction += press_directional_keypad(dx, dy)
            cx, cy = nx, ny
        instructions3.append(instruction)
    print(instructions3[-1])

    instr_lengths = [len(x) for x in instructions3]
    print(
        [
            (num, l, instruction)
            for num, l, instruction in zip(nums, instr_lengths, instructions3)
        ]
    )
    result = sum([a * b for a, b in zip(instr_lengths, nums)])
    return result


res_example = main("2024/day21_example.txt")
print(res_example)
res_actual = main("2024/day21_input.txt")
print(res_actual)
