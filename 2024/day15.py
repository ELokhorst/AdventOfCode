def read_layout(layout, pt2=True) -> dict:
    if pt2:
        replacements = [(".", ".."), ("#", "##"), ("O", "[]"), ("@", "@.")]
        for org, new in replacements:
            layout = [line.replace(org, new) for line in layout]
        for line in layout:
            print(line)
    coords = {(x, y): char for y, l in enumerate(layout) for x, char in enumerate(l)}
    return coords


def update_coords(coords: dict, instruction: str):
    current_position = [k for k, v in coords.items() if v == "@"][0]
    dy = -1 if instruction == "^" else 1 if instruction == "v" else 0
    dx = 1 if instruction == ">" else -1 if instruction == "<" else 0
    next_pos = (current_position[0] + dx, current_position[1] + dy)
    # print(next_pos)
    if coords[next_pos] == ".":
        coords[next_pos] = "@"
        coords[current_position] = "."
    elif coords[next_pos] == "O":
        move = [next_pos]
        while coords[next_pos] == "O":
            next_pos = (next_pos[0] + dx, next_pos[1] + dy)
            move.append(next_pos)
        if coords[next_pos] == ".":
            coords[current_position] = "."
            coords[move.pop(0)] = "@"
            for coord in move:
                coords[coord] = "O"
    return coords


def part2(coords: dict, instruction: str):
    current_position = [k for k, v in coords.items() if v == "@"][0]
    dy = -1 if instruction == "^" else 1 if instruction == "v" else 0
    dx = 1 if instruction == ">" else -1 if instruction == "<" else 0
    next_pos = (current_position[0] + dx, current_position[1] + dy)
    direction = (dx, dy)
    # print(next_pos)
    if coords[next_pos] == ".":
        coords[next_pos] = "@"
        coords[current_position] = "."
    elif coords[next_pos] in ["[", "]"]:
        move = [next_pos]
        while coords[next_pos] == "O":
            next_pos = (next_pos[0] + dx, next_pos[1] + dy)
            move.append(next_pos)
        if coords[next_pos] == ".":
            coords[current_position] = "."
            coords[move.pop(0)] = "@"
            for coord in move:
                coords[coord] = "O"
    return coords


def main(file: str):
    with open(file, "r", encoding="utf-8") as f:
        content = f.read().strip().split("\n\n")

    coords, instructions = read_layout(content[0].splitlines()), list(content[1])
    while instructions:
        instruction = instructions.pop(0)
        # print(instruction)
        coords = update_coords(coords, instruction)

    return sum(
        [100 * coord[1] + coord[0] for coord, val in coords.items() if val == "O"]
    )


res_example = main("2024/day15_example.txt")
print(res_example)
# res_actual = main("2024/day15_input.txt")
# print(res_actual)
