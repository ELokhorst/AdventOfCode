def similarity_score(file: str) -> int:
    list_left, list_right = zip(
        *[map(int, line.split()) for line in open(file, encoding="utf-8")]
    )
    part1 = sum([abs(r - l) for r, l in zip(sorted(list_left), sorted(list_right))])

    counts_map = [list_right.count(x) for x in list_left]
    part2 = sum([l * r for l, r in zip(list_left, counts_map)])
    return part1, part2


res_example = similarity_score("2024/day01_example.txt")
print(res_example)
res_actual = similarity_score("2024/day01_input.txt")
print(res_actual)
