from hashlib import md5


def main(file: str):
    with open(file, "r", encoding="utf-8") as f:
        puzzle_input = f.read().strip()

    num = 0
    while True:
        str2hash = puzzle_input + str(num)
        if md5(str2hash.encode()).hexdigest().startswith("000000"):
            break
        num += 1
    return num


res_example = main("2015/day04_example.txt")
print(res_example)
res_actual = main("2015/day04_input.txt")
print(res_actual)
