def pairwise_diff_sum(file: str) -> int:
    list_left, list_right = zip(
        *[map(int, line.split()) for line in open(file, encoding="utf-8")]
    )
    summed = sum([abs(r - l) for r, l in zip(sorted(list_left), sorted(list_right))])
    return summed


res_example = pairwise_diff_sum("day1_example.csv")
print(res_example)
res_actual = pairwise_diff_sum("day1_input.csv")
print(res_actual)


def similarity_score(file: str) -> int:
    list_left, list_right = zip(
        *[map(int, line.split()) for line in open(file, encoding="utf-8")]
    )
    counts_map = [list_right.count(x) for x in list_left]
    total = sum([l * r for l, r in zip(list_left, counts_map)])
    return total


res_example = similarity_score("day1_example.csv")
print(res_example)
res_actual = similarity_score("day1_input.csv")
print(res_actual)
