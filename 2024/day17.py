def main(file: str):
    with open(file, "r", encoding="utf-8") as f:
        lines = f.read().strip().split("\n\n")

    registers = lines[0].splitlines()
    program = list(map(int, (lines[1].split(": ")[1]).split(",")))
    return registers, program


res_example = main("2024/day17_example.txt")
print(res_example)
res_actual = main("2024/day17_input.txt")
print(res_actual)
