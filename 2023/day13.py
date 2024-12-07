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


def check_mirror(pattern: list[str]) -> int:
    i = 0
    for idx, row in enumerate(pattern[:-1]):
        if row == pattern[idx + 1]:
            while True:
                left_index = idx - i
                right_index = idx + i + 1

                if left_index < 0 or right_index >= len(pattern):
                    print(
                        f"Reached {'left' if left_index < 0 else 'right'} boundary for index: {idx}"
                    )
                    return idx + 1

                if pattern[left_index] != pattern[right_index]:
                    print(
                        f"Mismatch at left_index: {left_index} and right_index: {right_index}"
                    )
                    break

                i += 1
    return 0


def summarize_notes(file: str) -> int:
    h, v = read_patterns(file)

    totals = 0
    for h_p in h:
        mirror_h = check_mirror(h_p)
        print(f"Adding {100 * mirror_h}")
        totals += 100 * mirror_h

    for v_p in v:
        mirror_v = check_mirror(v_p)
        print(f"Adding {mirror_v}")
        totals += mirror_v

    return totals


res_example = summarize_notes("2023/day13_example.txt")
print(res_example)
res_actual = summarize_notes("2023/day13_input.txt")
print(res_actual)
