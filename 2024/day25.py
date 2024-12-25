import numpy as np


def main(file: str):
    with open(file, "r", encoding="utf-8") as f:
        content = f.read().strip().replace(".", "0").replace("#", "1")

    schematics = [
        np.array(
            [list(map(int, list(line))) for line in schema.splitlines()]
        ).T.tolist()
        for schema in content.split("\n\n")
    ]

    locks = [
        [line for line in schematic]
        for schematic in schematics
        if all(line[0] == 1 for line in schematic)
    ]
    keys = [
        [line for line in schematic]
        for schematic in schematics
        if all(line[0] == 0 for line in schematic)
    ]

    fit = 0
    for lock in locks:
        for key in keys:
            overlap_matrix = sum([np.array(lock), np.array(key)])
            if np.all(overlap_matrix <= 1):
                fit += 1

    return fit


res_example = main("2024/day25_example.txt")
print(res_example)
res_actual = main("2024/day25_input.txt")
print(res_actual)
