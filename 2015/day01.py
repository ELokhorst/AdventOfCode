def main(file: str):
    with open(file, "r", encoding="utf-8") as f:
        instructions = f.read().strip()

    floor = 0
    for i, instr in enumerate(instructions):
        floor += 1 if instr == "(" else -1
        if floor < 0:
            return i + 1
    return floor


res_example = main("2015/day01_example.txt")
print(res_example)
res_actual = main("2015/day01_input.txt")
print(res_actual)
