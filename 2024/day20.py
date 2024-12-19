def main(file: str):
    with open(file, "r", encoding="utf-8") as f:
        content = f.read().strip().split("\n\n")

    return content


res_example = main("2024/day20_example.txt")
print(res_example)
res_actual = main("2024/day20_input.txt")
print(res_actual)
