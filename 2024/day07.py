import itertools


def apply_operators(values, operators):
    result = values[0]
    for i, op in enumerate(operators):
        if op == 0:
            result += values[i + 1]
        elif op == 1:
            result *= values[i + 1]
        elif op == 2:
            result = int(str(result) + str(values[i + 1]))
    return result


def main(file: str):
    with open(file, "r", encoding="utf-8") as f:
        lines = f.read().strip().split("\n")

    total_sum = 0
    for line in lines:
        answer, equation = int(line.split(": ")[0]), list(
            map(int, line.split(": ")[1].split())
        )

        for operators in itertools.product(range(3), repeat=len(equation) - 1):
            if apply_operators(equation, operators) == answer:
                total_sum += answer
                break

    return total_sum


res_example = main("2024/day07_example.txt")
print(res_example)
res_actual = main("2024/day07_input.txt")
print(res_actual)
