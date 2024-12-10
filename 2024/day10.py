def traverse(coords: list[tuple], trail: set, current_pos: tuple):
    surr_coords = [
        (current_pos[0] - 1, current_pos[1]),
        (current_pos[0] + 1, current_pos[1]),
        (current_pos[0], current_pos[1] - 1),
        (current_pos[0], current_pos[1] + 1),
    ]

    valid = [
        coord
        for coord in coords
        if coord[2] != "."
        and coord not in trail
        and (coord[0], coord[1]) in surr_coords
        and int(current_pos[2]) + 1 == int(coord[2])
    ]

    valid_ends = 0
    for valid_coord in valid:
        if valid_coord[2] == "9":
            valid_ends += 1
        else:
            trail.add(current_pos)
            valid_ends += traverse(coords, trail, valid_coord)
            trail.remove(current_pos)  # backtrack

    return valid_ends


def main(file: str):
    with open(file, "r", encoding="utf-8") as f:
        maps = f.read().split("\n\n")

    total_routes = []
    for m in maps:
        print("Starting new map")
        coords = {
            (i, j, height)
            for i, line in enumerate(m.splitlines())
            for j, height in enumerate(line)
        }

        trailheads = [coord for coord in coords if coord[2] == "0"]
        scores = [traverse(coords, set(), trailhead) for trailhead in trailheads]
        total_routes.append(sum(scores))
    return total_routes


res_example = main("2024/day10_example.txt")
print(res_example)
res_actual = main("2024/day10_input.txt")
print(res_actual)
