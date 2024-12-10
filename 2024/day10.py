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
        for surr_coord in surr_coords
        if coord[2] != "."
        and coord[0] == surr_coord[0]
        and coord[1] == surr_coord[1]
        and coord not in trail
        and int(current_pos[2]) + 1 == int(coord[2])
    ]

    valid_ends = 0
    for valid_coord in valid:
        if valid_coord[2] == "9":
            valid_ends += 1
        else:
            trail.add(current_pos)
            current_pos = valid_coord
            valid_ends += traverse(coords, trail.copy(), current_pos)
    return valid_ends


def main(file: str):
    with open(file, "r", encoding="utf-8") as f:
        maps = f.read().split("\n\n")

    total_routes = []
    for map in maps:
        print("Starting new map")
        coords = set(
            [
                (i, j, height)
                for i, l in enumerate(map.splitlines())
                for j, height in enumerate(l)
            ]
        )
        trailheads = [coord for coord in coords if coord[2] == "0"]
        results = []
        for trailhead in trailheads:
            trail = set()
            current_pos = trailhead
            score = traverse(coords, trail, current_pos)
            results.append(score)
        total_routes.append(sum(results))
    return total_routes


res_example = main("2024/day10_example.txt")
print(res_example)
res_actual = main("2024/day10_input.txt")
print(res_actual)
