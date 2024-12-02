import time


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
    for i in range(len(report)):
        list_leftout = report[:i] + report[i + 1 :]
        if determine_safety(list_leftout):
            return 1
    return 0


def run_reports(file: str) -> tuple[int, int]:
    start = time.time()
    reports = [
        list(map(int, line.split())) for line in open(file, "r", encoding="utf-8")
    ]
    safe_count = sum([determine_safety(report) for report in reports])
    tolerated_count = sum([determine_tolerated_safety(report) for report in reports])
    end = time.time()
    print(f"Total time: {(end-start) * 10**3}")
    return safe_count, tolerated_count


res_example = run_reports("2024/day02_example.csv")
print(res_example)
res_actual = run_reports("2024/day02_input.csv")
print(res_actual)
