import re


def parse_do_dont(content: str):
    pattern_do = r"(^|do(?!n\'t))(.*?)(don't|$)"
    matches = [match[1] for match in re.findall(pattern_do, content)]
    print(matches)
    new_content = "".join(matches)
    return new_content


def get_noncorrupted(file: str, part2: bool = False):
    with open(file, "r", encoding="utf-8") as f:
        content = f.read()

    if part2:
        content = parse_do_dont(content.replace("\n", ""))
        print(content)

    mul_pattern = r"mul\(\d{1,3},\d{1,3}\)"
    compute_pattern = r"(\d+),(\d+)"
    matches = re.findall(mul_pattern, content)
    result = sum(
        [
            int(x) * int(y)
            for match in matches
            for x, y in re.findall(compute_pattern, match)
        ]
    )
    return result


res_example = get_noncorrupted("2024/day03_example.txt")
print(res_example)
res_actual = get_noncorrupted("2024/day03_input.txt")
print(res_actual)


res_example = get_noncorrupted("2024/day03_example.txt", part2=True)
print(res_example)
res_actual = get_noncorrupted("2024/day03_input.txt", part2=True)
print(res_actual)
