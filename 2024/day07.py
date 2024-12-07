import itertools


def apply_operators(values, operators):
    operator_map = {
        0: lambda x, y: x + y,
        1: lambda x, y: x * y,
        2: lambda x, y: int(str(x) + str(y)),
    }
    result = values[0]
    for i, op in enumerate(operators):
        fn = operator_map[op]
        result = fn(result, values[i + 1])
    return result


def main(file: str):
    with open(file, "r", encoding="utf-8") as f:
        lines = f.read().split("\n")

    totals = 0
    equations = [line.split(": ") for line in lines]  # ['156', '11 17 18']
    operators = [0, 1, 2]
    for equation in equations:
        answer = int(equation[0])  # 156
        equation = list(map(int, equation[1].split(" ")))  # [11, 17, 18]
        combinations = itertools.product(operators, repeat=len(equation) - 1)
        for c in combinations:
            result = apply_operators(equation, c)
            if result == answer:
                totals += answer
                break

    return totals


res_example = main("2024/day07_example.txt")
print(res_example)
res_actual = main("2024/day07_input.txt")
print(res_actual)
