def is_consistent(report: list[int]) -> bool:
    return report == sorted(report) or report == sorted(report, reverse=True)


def determine_safety(report: list[int]) -> int:
    if is_consistent(report):
        unsafe_count = sum(
            1
            for i in range(len(report) - 1)
            if not (1 <= abs(report[i] - report[i + 1]) <= 3)
        )
        if unsafe_count == 0:
            return 1
    return 0


def determine_tolerated_safety(report: list[int]) -> int:
    if determine_safety(report):
        return 1
    for level_leftout in report:
        if determine_safety([level for level in report if level != level_leftout]):
            return 1
    return 0


def run_reports(file: str) -> tuple[int, int]:
    reports = [
        list(map(int, line.split())) for line in open(file, "r", encoding="utf-8")
    ]
    safe_count = sum([determine_safety(report) for report in reports])
    tolerated_count = sum([determine_tolerated_safety(report) for report in reports])
    return safe_count, tolerated_count


res_example = run_reports("day2_example.csv")
print(res_example)
res_actual = run_reports("day2_input.csv")
print(res_actual)
