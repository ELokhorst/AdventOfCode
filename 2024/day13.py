from ortools.sat.python import cp_model


def solve_puzzle(puzzle, part2: bool):
    if part2:
        puzzle[2][0] += 10**13
        puzzle[2][1] += 10**13

    model = cp_model.CpModel()

    a = model.NewIntVar(0, int(1e15), "a")
    b = model.NewIntVar(0, int(1e15), "b")

    model.Add(puzzle[0][0] * a + puzzle[1][0] * b == puzzle[2][0])
    model.Add(puzzle[0][1] * a + puzzle[1][1] * b == puzzle[2][1])

    model.Minimize(3 * a + b)

    solver = cp_model.CpSolver()
    status = solver.Solve(model)

    if status == cp_model.OPTIMAL or status == cp_model.FEASIBLE:
        solution = (solver.Value(a), solver.Value(b))
        return solution
    elif status == cp_model.INFEASIBLE:
        return "No solution exists (infeasible)"
    else:
        return "Something went wrong"


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
        res = solve_puzzle(puzzle, True)
        if isinstance(res, tuple):
            tokens += res[0] * 3 + res[1]
    return tokens


res_example = main("2024/day13_example.txt")
print(res_example)
res_actual = main("2024/day13_input.txt")
print(res_actual)
