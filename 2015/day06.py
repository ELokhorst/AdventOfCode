from re import findall


def main(file):
    with open(file, "r", encoding="utf-8") as f:
        content = f.read().strip().splitlines()

    grid = [[0 for _ in range(1000)] for _ in range(1000)]

    operations = [
        0 if "off" in line else 1 if "toggle" in line else 2 for line in content
    ]
    nums = [[int(n) for n in findall(r"(\d+)", line)] for line in content]
    commands = list(zip(operations, nums))

    for operation, (x1, y1, x2, y2) in commands:
        print(operation)
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                if operation == 0:
                    grid[x][y] = max(0, grid[x][y] - 1)
                elif operation == 1:
                    grid[x][y] += 2
                elif operation == 2:
                    grid[x][y] += 1

        # for row in grid:
        #     print(row)
    lights_on = sum([light for row in grid for light in row])
    return lights_on


res_example = main("2015/day06_example.txt")
print(res_example)
res_actual = main("2015/day06_input.txt")
print(res_actual)
