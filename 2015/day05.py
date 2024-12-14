def main(file: str):
    with open(file, "r", encoding="utf-8") as f:
        strings = f.read().strip().splitlines()

    nice = 0
    for s in strings:
        print(s)
        # contains_three_vowels = (
        #     sum([s.count(ss) for ss in ["a", "e", "i", "o", "u"]]) >= 3
        # )
        contains_pair = any(s[i] + s[i + 1] in s[i + 2 :] for i in range(len(s) - 2))
        double_letter = any([s[i] == s[i + 2] for i in range(len(s) - 2)])
        # not_contain = any(ss in s for ss in ["ab", "cd", "pq", "xy"])
        if all([contains_pair, double_letter]):
            nice += 1
    return nice


res_example = main("2015/day05_example.txt")
print(res_example)
res_actual = main("2015/day05_input.txt")
print(res_actual)
