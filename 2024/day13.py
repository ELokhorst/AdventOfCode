import numpy as np


def solve_puzzle(puzzle, part2: bool):
    if part2:
        puzzle[2][0] += 10000000000000
        puzzle[2][1] += 10000000000000
    a = np.array([[puzzle[0][0], puzzle[1][0]], [puzzle[0][1], puzzle[1][1]]])
    b = np.array([puzzle[2][0], puzzle[2][1]])

    try:
        det = np.linalg.det(a)
        if det == 0:
            if np.linalg.matrix_rank(a) < 2:
                return "No solution exists (rank deficient)"
        else:
            solution = np.linalg.solve(a, b)
            if all(np.isclose(val, round(val)) for val in solution):
                solution = tuple(map(int, np.round(solution)))
            else:
                return "No integer solution exists for the given puzzle"
    except Exception as e:
        return str(e)

    return solution


def main(file: str):
    with open(file, "r", encoding="utf-8") as f:
        puzzles = f.read().strip().split("\n\n")

    puzzles = [
        [line.split(": ")[1].split(", ") for line in puzzle.splitlines()]
        for puzzle in puzzles
    ]
    puzzles = [
        [
            [
                int(item.split("+")[1]) if "+" in item else int(item.split("=")[1])
                for item in sublist
            ]
            for sublist in puzzle
        ]
        for puzzle in puzzles
    ]

    tokens = 0
    for puzzle in puzzles:
        res = solve_puzzle(puzzle, False)
        if isinstance(res, tuple):
            tokens += res[0] * 3 + res[1]
    return tokens


res_example = main("2024/day13_example.txt")
print(res_example)
res_actual = main("2024/day13_input.txt")
print(res_actual)
