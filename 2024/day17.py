from re import findall


def main(file: str):
    with open(file, "r", encoding="utf-8") as f:
        a, b, c, *program = [int(n) for n in findall("(\d+)", f.read())]

    out = []
    i = 0
    while 0 <= i < len(program):
        operand = program[i + 1]
        combo_op = [0, 1, 2, 3, a, b, c, None][operand]

        print(f"Opcode: {program[i]}. Operand: {operand}. Combo_op: {combo_op}")

        match (program[i]):
            case 0:
                a = int(a / 2**combo_op)
            case 1:
                b = b ^ operand
            case 2:
                b = combo_op % 8
            case 3:
                i = i if a == 0 else operand - 2
            case 4:
                b = b ^ c
            case 5:
                out.append(combo_op % 8)
            case 6:
                b = int(a / 2**combo_op)
            case 7:
                c = int(a / 2**combo_op)

        i += 2

    return ",".join([str(val) for val in out])


res_example = main("2024/day17_example.txt")
print(res_example)
# res_actual = main("2024/day17_input.txt")
# print(res_actual)
