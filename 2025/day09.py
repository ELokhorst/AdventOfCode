from itertools import combinations


def main(file: str):
    with open(file, "r", encoding="utf-8") as f:
        lines = f.read().splitlines()

    max_area = 0
    coords = [tuple(map(int, line.split(","))) for line in lines]
    for coord_a, coord_b in list(combinations(coords, 2)):
        x_val = abs(coord_a[0] - coord_b[0]) + 1
        y_val = abs(coord_a[1] - coord_b[1]) + 1
        area = x_val * y_val
        if area > max_area:
            max_area = area
    return max_area


res_example = main("2025/day09_example.txt")
print(res_example)
# res_actual = main("2025/day09_input.txt")
# print(res_actual)
