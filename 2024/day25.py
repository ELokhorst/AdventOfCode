import numpy as np


def main(file: str):
    with open(file, "r", encoding="utf-8") as f:
        content = f.read().strip().replace(".", "0").replace("#", "1")

    schematics = [
        [list(map(int, list(line))) for line in schema.splitlines()]
        for schema in content.split("\n\n")
    ]

    for schema in schematics:
        print(np.array(schema).T.tolist())
        print("\n")

    return schematics


res_example = main("2024/day25_example.txt")
print(res_example)
# res_actual = main("2024/day25_input.txt")
# print(res_actual)
