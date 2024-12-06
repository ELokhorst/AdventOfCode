from enum import unique


def find_obstacle(objects, guard_pos, direction):
    obstacle = None
    if direction == "up":
        expression = list(
            (x, y) for (x, y) in objects if y < guard_pos[1] and x == guard_pos[0]
        )
        if expression:
            obstacle = min(expression, key=lambda coord: guard_pos[1] - coord[1])
    elif direction == "right":
        expression = list(
            (x, y) for (x, y) in objects if y == guard_pos[1] and x > guard_pos[0]
        )
        if expression:
            obstacle = min(expression, key=lambda coord: coord[0] - guard_pos[0])
    elif direction == "down":
        expression = list(
            (x, y) for (x, y) in objects if y > guard_pos[1] and x == guard_pos[0]
        )
        if expression:
            obstacle = min(expression, key=lambda coord: coord[1] - guard_pos[1])
    if direction == "left":
        expression = list(
            (x, y) for (x, y) in objects if y == guard_pos[1] and x < guard_pos[0]
        )
        if expression:
            obstacle = min(expression, key=lambda coord: guard_pos[0] - coord[0])
    return obstacle


def distance_to_edge(coords, guard_pos, direction):
    return [
        (x, y)
        for (x, y), _ in coords
        if (direction == "up" and x == guard_pos[0] and y <= guard_pos[1])
        or (direction == "right" and y == guard_pos[1] and guard_pos[0] <= x)
        or (direction == "down" and x == guard_pos[0] and guard_pos[1] <= y)
        or (direction == "left" and y == guard_pos[1] and x <= guard_pos[0])
    ]


def update_guard_pos(coords, objects, guard_pos, direction, visited: list):
    obstacle = find_obstacle(objects, guard_pos, direction)
    if not obstacle:
        # visited.extend(distance_to_edge(coords, guard_pos, direction))
        return (
            (guard_pos, None),
            False,
        )
    # visited.extend(
    #     [
    #         (x, y)
    #         for (x, y), _ in coords
    #         if (
    #             direction == "up"
    #             and x == obstacle[0] == guard_pos[0]
    #             and obstacle[1] < y <= guard_pos[1]
    #         )
    #         or (
    #             direction == "right"
    #             and y == obstacle[1] == guard_pos[1]
    #             and guard_pos[0] <= x < obstacle[0]
    #         )
    #         or (
    #             direction == "down"
    #             and x == obstacle[0] == guard_pos[0]
    #             and guard_pos[1] <= y < obstacle[1]
    #         )
    #         or (
    #             direction == "left"
    #             and y == obstacle[1] == guard_pos[1]
    #             and obstacle[0] < x <= guard_pos[0]
    #         )
    #     ]
    # )
    if direction == "up":
        return ((obstacle[0], obstacle[1] + 1), direction), True
    elif direction == "right":
        return ((obstacle[0] - 1, obstacle[1]), direction), True
    elif direction == "down":
        return ((obstacle[0], obstacle[1] - 1), direction), True
    elif direction == "left":
        return ((obstacle[0] + 1, obstacle[1]), direction), True


def walkthrough(coords, objects):
    directions = ["up", "right", "down", "left"]
    i = 0
    guard_pos = ([coords for coords, token in coords if token == "^"][0], None)
    guard_positions = set()
    visited = []

    loop = False
    while True:
        direction = directions[i]
        guard_pos, continue_loop = update_guard_pos(
            coords, objects, guard_pos[0], direction, visited
        )

        if not continue_loop:
            break

        if guard_pos in guard_positions:
            print(f"Found loop for {guard_pos} in {guard_positions}")
            loop = True
            break

        guard_positions.add(guard_pos)
        i = (i + 1) % 4

    return loop


def main(file: str):
    with open(file, "r", encoding="utf-8") as f:
        content = f.read()

    layout = content.split("\n")
    coords_token = [[(i, j), m] for j, l in enumerate(layout) for i, m in enumerate(l)]
    print(f"Grid is: {len(layout)} * {len(layout[0])}")

    loop = 0
    for coord, token in coords_token:
        if not token == ".":
            continue
        # print(f"Creating object at: {coord}")
        objects = [coords for coords, token in coords_token if token == "#"] + [coord]
        result = walkthrough(coords_token, objects)
        if result:
            loop += 1

    return loop


res_example = main("2024/day06_example.txt")
print(res_example)
res_actual = main("2024/day06_input.txt")
print(res_actual)
