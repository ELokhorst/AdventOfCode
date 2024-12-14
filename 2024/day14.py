import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colormaps


def load_puzzle(file):
    with open(file, "r", encoding="utf-8") as f:
        content = f.read().strip().splitlines()

    pvs = [
        [(int(px), int(py)), (int(vx), int(vy))]
        for line in content
        for p, v in [line.split(" ")]
        for px, py in [p.split("=")[1].split(",")]
        for vx, vy in [v.split("=")[1].split(",")]
    ]

    return pvs


def coordinates_to_map(coordinates, width, height, title):
    grid = np.zeros((height, width), dtype=int)

    for x, y in coordinates:
        if 0 <= x < width and 0 <= y < height:
            grid[y, x] = 1

    filename = f"2024/xmas/{title}.png"
    plt.imsave(filename, grid, cmap=colormaps["binary_r"], format="png", dpi=300)


def add_with_teleport(a, b, max_value, start_value=0):
    return start_value + ((a + b - start_value) % (max_value - 1 - start_value + 1))


def main(file: str):
    pvs = load_puzzle(file)
    len_grid_x = 101
    len_grid_y = 103
    seconds = 100
    for s in range(seconds):
        for i, (pos, vel) in enumerate(pvs):
            new_x = add_with_teleport(pos[0], vel[0], len_grid_x)
            new_y = add_with_teleport(pos[1], vel[1], len_grid_y)
            pvs[i][0] = (new_x, new_y)
        coordinates_to_map([p for p, _ in pvs], len_grid_x, len_grid_y, str(s))
    q1 = [p for p, _ in pvs if p[0] < len_grid_x // 2 and p[1] < len_grid_y // 2]
    q2 = [p for p, _ in pvs if p[0] > len_grid_x // 2 and p[1] < len_grid_y // 2]
    q3 = [p for p, _ in pvs if p[0] > len_grid_x // 2 and p[1] > len_grid_y // 2]
    q4 = [p for p, _ in pvs if p[0] < len_grid_x // 2 and p[1] > len_grid_y // 2]
    return len(q1) * len(q2) * len(q3) * len(q4)


# res_example = main("2024/day14_example.txt")
# print(res_example)
res_actual = main("2024/day14_input.txt")
print(res_actual)
