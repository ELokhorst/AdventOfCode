from itertools import combinations


def calc_top_coords(comb, i):
    return (
        comb[0][0] - (comb[1][0] - comb[0][0]) * i,
        comb[0][1] + (comb[0][1] - comb[1][1]) * i,
    )


def calc_bot_coords(comb, i):
    return (
        comb[1][0] + (comb[1][0] - comb[0][0]) * i,
        comb[1][1] - (comb[0][1] - comb[1][1]) * i,
    )


def calculate_new_coordinates(comb, max_x, max_y):
    """Calculate new coordinates based on the given combination."""
    new_coords = []
    i = 1
    new_coords.append(calc_bot_coords(comb, i))
    while max_x >= new_coords[-1][0] >= 0 and max_y >= new_coords[-1][1] >= 0:
        i += 1
        new_coords.append(calc_bot_coords(comb, i))

    i = 1
    new_coords.append(calc_top_coords(comb, i))
    while max_x >= new_coords[-1][0] >= 0 and max_y >= new_coords[-1][1] >= 0:
        i += 1
        new_coords.append(calc_top_coords(comb, i))

    new_coords.extend([cd for cd in comb])
    return new_coords


def main(file: str):
    with open(file, "r", encoding="utf-8") as f:
        lines = f.read().strip().split("\n")

    antennas = [
        [(i, j), char] for i, line in enumerate(lines) for j, char in enumerate(line)
    ]
    all_coords = set([antenna[0] for antenna in antennas])
    unique = set([antenna[1] for antenna in antennas if antenna[1] != "."])
    antisignals = set()
    for char in unique:
        coords = [coord for (coord, c) in antennas if c == char]
        if len(coords) >= 2:
            combs = list(combinations(coords, 2))

            for comb in combs:
                for new in calculate_new_coordinates(comb, len(lines[0]), len(lines)):
                    if new in all_coords:
                        antisignals.add(new)

    return len(antisignals)


res_example = main("2024/day08_example.txt")
print(res_example)
res_actual = main("2024/day08_input.txt")
print(res_actual)
