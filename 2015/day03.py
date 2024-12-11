def update_pos(char, pos):
    if char == ">":
        return (pos[0] + 1, pos[1])
    elif char == "<":
        return (pos[0] - 1, pos[1])
    elif char == "^":
        return (pos[0], pos[1] + 1)
    elif char == "v":
        return (pos[0], pos[1] - 1)


def walk_route(route: dict, pos, direction):
    if not route.get(pos):
        route[pos] = 1
    else:
        route[pos] += 1
    new_pos = update_pos(direction, pos)
    return new_pos


def main(file: str):
    with open(file, "r", encoding="utf-8") as f:
        file = f.read().strip().splitlines()

    for directions in file:
        route1 = {}
        route2 = {}
        pos1 = (0, 0)
        pos2 = (0, 0)
        for i, direction in enumerate(directions):
            if i % 2 == 0:
                pos1 = walk_route(route1, pos1, direction)
            else:
                pos2 = walk_route(route2, pos2, direction)
        walk_route(route1, pos1, direction)
        walk_route(route2, pos2, direction)

    route1.update(route2)
    visited = sum([1 for count in route1.values() if count > 0])
    return visited


res_example = main("2015/day03_example.txt")
print(res_example)
res_actual = main("2015/day03_input.txt")
print(res_actual)
