def pairwise_diff_sum(l_l: list, l_r: list) -> int:
    summed = sum([abs(r - l) for r, l in zip(sorted(l_l), sorted(l_r))])
    return summed


list_left, list_right = zip(
    *[map(int, line.split()) for line in open("day1_input.csv", encoding="utf-8")]
)

example1 = [3, 4, 2, 1, 3, 3]
example2 = [4, 3, 5, 3, 9, 3]
res_example = pairwise_diff_sum(example1, example2)
print(res_example)
res_actual = pairwise_diff_sum(list_left, list_right)
print(res_actual)


def similarity_score(l_l: list, l_r: list) -> int:
    counts_map = [l_r.count(x) for x in l_l]
    total = sum([l * r for l, r in zip(l_l, counts_map)])
    return total


res_example = similarity_score(example1, example2)
print(res_example)
res_actual = similarity_score(list_left, list_right)
print(res_actual)
