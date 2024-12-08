from itertools import combinations


def calculate_new_coordinates(comb, max_x, max_y):
    """Calculate new coordinates based on the given combination."""

    def calculate_coords(base, other, max_x, max_y):
        """Calculate a series of coordinates in the specified direction."""
        coords = []
        i = 1
        while True:
            x = base[0] + (base[0] - other[0]) * i
            y = base[1] + (base[1] - other[1]) * i
            if not (0 <= x <= max_x and 0 <= y <= max_y):
                break
            coords.append((x, y))
            i += 1
        return coords

    bottom_coords = calculate_coords(comb[1], comb[0], max_x, max_y)
    top_coords = calculate_coords(comb[0], comb[1], max_x, max_y)

    return bottom_coords + top_coords + list(comb)


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
