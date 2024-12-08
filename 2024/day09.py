def main(file: str):
    with open(file, "r", encoding="utf-8") as f:
        lines = f.read().strip().split("\n")

    return lines


res_example = main("2024/day09_example.txt")
print(res_example)
res_actual = main("2024/day09_input.txt")
print(res_actual)
