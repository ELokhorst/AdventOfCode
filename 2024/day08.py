from itertools import combinations


def calculate_new_coordinates(comb):
    """Calculate new coordinates based on the given combination."""
    new_coords = [
        (
            comb[0][0] - (comb[1][0] - comb[0][0]),
            comb[0][1] + (comb[0][1] - comb[1][1]),
        ),
        (
            comb[1][0] + (comb[1][0] - comb[0][0]),
            comb[1][1] - (comb[0][1] - comb[1][1]),
        ),
    ]
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
                for new in calculate_new_coordinates(comb):
                    if new in all_coords:
                        antisignals.add(new)

    return len(antisignals)


res_example = main("2024/day08_example.txt")
print(res_example)
res_actual = main("2024/day08_input.txt")
print(res_actual)
