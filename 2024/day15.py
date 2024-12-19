def read_layout(layout, pt2=True) -> dict:
    if pt2:
        replacements = [(".", ".."), ("#", "##"), ("O", "[]"), ("@", "@.")]
        for org, new in replacements:
            layout = [line.replace(org, new) for line in layout]
    for line in layout:
        print(line)
    coords = {(x, y): char for y, l in enumerate(layout) for x, char in enumerate(l)}
    return coords


def print_grid(grid_dict):
    max_x = max(key[0] for key in grid_dict.keys())
    max_y = max(key[1] for key in grid_dict.keys())

    grid = [["." for _ in range(max_x + 1)] for _ in range(max_y + 1)]

    for (x, y), value in grid_dict.items():
        grid[y][x] = value

    for row in grid:
        print("".join(row))


def get_boxes_to_move(coords: dict, instruction: str, robot_pos: tuple):
    dy = -1 if instruction == "^" else 1 if instruction == "v" else 0
    dx = 1 if instruction == ">" else -1 if instruction == "<" else 0

    stack = [robot_pos]
    visited = set()
    i = 0

    while i < len(stack):
        x, y = stack[i]
        nx, ny = x + dx, y + dy
        cchar = coords.get((nx, ny), None)

        if cchar == "#":
            return [], (0, 0)

        if (nx, ny) not in visited and cchar in "O[]":
            stack.append((nx, ny))
            visited.add((nx, ny))
            if cchar == "]":
                stack.append((nx - 1, ny))
            elif cchar == "[":
                stack.append((nx + 1, ny))

        i += 1

    return stack, (dx, dy)


def main(file: str):
    with open(file, "r", encoding="utf-8") as f:
        content = f.read().strip().split("\n\n")

    coords = read_layout(content[0].splitlines())
    instructions = list(content[1])
    robot_pos = next(k for k, v in coords.items() if v == "@")

    for instruction in instructions:
        boxes_to_move, (dx, dy) = get_boxes_to_move(coords, instruction, robot_pos)
        if boxes_to_move:
            for x, y in reversed(boxes_to_move):
                coords[x + dx, y + dy] = coords[x, y]
                coords[x, y] = "."
            robot_pos = (robot_pos[0] + dx, robot_pos[1] + dy)

    print_grid(coords)
    result = sum(
        100 * coord[1] + coord[0] for coord, val in coords.items() if val == "["
    )
    return result


res_example = main("2024/day15_example.txt")
print(res_example)
res_actual = main("2024/day15_input.txt")
print(res_actual)
