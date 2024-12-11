def main(file: str):
    with open(file, "r", encoding="utf-8") as f:
        sizes = f.read().strip().splitlines()

    dimensions = [
        [x, y, z] for x, y, z in (map(int, size.split("x")) for size in sizes)
    ]
    ribbon = [x * y * z for x, y, z in dimensions]
    required = [
        sum(2 * dim for dim in sorted(dimension)[:2]) for dimension in dimensions
    ]
    total = [x + y for x, y in zip(required, ribbon)]
    return sum(total)


res_example = main("2015/day02_example.txt")
print(res_example)
res_actual = main("2015/day02_input.txt")
print(res_actual)
