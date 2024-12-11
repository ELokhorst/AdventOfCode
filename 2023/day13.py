def read_patterns(file: str):
    with open(file, "r", encoding="utf-8") as file:
        puzzles = file.read().split("\n\n")

    horizontal_patterns = [
        [line.strip() for line in puzzle.splitlines()] for puzzle in puzzles
    ]

    vertical_patterns = [
        ["".join(row[j] for row in h_pattern) for j in range(len(h_pattern[0]))]
        for h_pattern in horizontal_patterns
    ]

    return horizontal_patterns, vertical_patterns


def get_mm_count(list1, list2):
    mismatch_count = 0
    for a, b in zip(list1, list2):
        if a != b:
            mismatch_count += 1
            if mismatch_count > 1:
                return mismatch_count

    return mismatch_count


def check_mirror(pattern: list[str]) -> int:
    max_mm = 1
    for idx, _ in enumerate(pattern[:-1]):
        i = 0
        mm_count = 0
        while mm_count <= max_mm:
            left_index = idx - i
            right_index = idx + 1 + i

            # print(f"Checking {left_index}, {right_index}")
            if left_index < 0 or right_index >= len(pattern):
                return idx + 1

            # print(pattern[left_index])
            # print(pattern[right_index])
            mm = get_mm_count(pattern[left_index], pattern[right_index])
            mm_count += mm
            i += 1
    return 0


def summarize_notes(file: str) -> int:
    h, v = read_patterns(file)

    totals = 0
    for h_p, v_p in zip(h, v):
        mirror_h = check_mirror(h_p)
        # print(f"Adding {100 * mirror_h}")
        totals += 100 * mirror_h
        if mirror_h == 0:
            mirror_v = check_mirror(v_p)
            # print(f"Adding {mirror_v}")
            totals += mirror_v

    return totals


res_example = summarize_notes("2023/day13_example.txt")
print(res_example)
res_actual = summarize_notes("2023/day13_input.txt")
print(res_actual)
