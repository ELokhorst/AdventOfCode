def read_patterns(file: str):
    with open(file, "r", encoding="utf-8") as file:
        content = file.read()

    horizontal_patterns = []
    raw_patterns = content.split("\n\n")
    for raw_pattern in raw_patterns:
        lines = raw_pattern.strip().split("\n")
        if lines:
            horizontal_patterns.append(lines)

    vertical_patterns = [[] for _ in range(len(horizontal_patterns))]
    for i, h_pattern in enumerate(horizontal_patterns):
        pattern_size = len(h_pattern[0])
        v_pattern = []
        for j in range(pattern_size):
            column = "".join([row[j] for row in h_pattern])
            v_pattern.append(column)
        vertical_patterns[i] = v_pattern

    return horizontal_patterns, vertical_patterns


def check_mirror_idx(pattern: list[str], idx: int) -> int:
    print(f"Checking for mirror index: {idx} / {len(pattern)}")
    i = 0

    while True:
        left_index = idx - i
        right_index = idx + i + 1

        if left_index < 0 or right_index >= len(pattern):
            print(
                f"Reached {'left' if left_index < 0 else 'right'} boundary for index: {idx}"
            )
            return idx + 1

        if pattern[left_index] != pattern[right_index]:
            print(pattern[left_index])
            print(pattern[right_index])
            print(
                f"Mismatch at left_index: {left_index} and right_index: {right_index}"
            )
            return 0

        i += 1


def find_mirroring(pattern: list[str]) -> int:
    is_even = len(pattern) % 2 == 0
    print(f"Even pattern: {is_even}")
    mirror_index = len(pattern) // 2 - 1
    check = check_mirror_idx(pattern, mirror_index)
    if check:
        return check

    if not is_even:
        mirror_index = len(pattern) // 2
        check = check_mirror_idx(pattern, mirror_index)
    return check


def summarize_notes(file: str) -> int:
    h, v = read_patterns(file)

    totals = 0
    for h_p in h:
        print("Horizontal pattern")
        [print(line) for line in h_p]
        mirror_h = find_mirroring(h_p)
        print(f"Adding {100 * mirror_h}")
        totals += 100 * mirror_h

    for v_p in v:
        print("Vertical pattern")
        [print(line) for line in v_p]
        mirror_v = find_mirroring(v_p)
        print(f"Adding {mirror_v}")
        totals += mirror_v

    return totals


res_example = summarize_notes("2023/day13_example.txt")
print(res_example)
res_actual = summarize_notes("2023/day13_input.txt")
print(res_actual)
