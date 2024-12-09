def main(file: str):
    with open(file, "r", encoding="utf-8") as f:
        disk = f.read().strip()

    num = 0
    files_list = [
        size * ([num] if i % 2 == 0 else [-1])
        for i, size in enumerate(map(int, disk))
        if not (i % 2) or (num := num + 1)
    ]

    for file in reversed(files_list[2::2]):
        suitable_space = None
        free = [(i, l) for i, l in enumerate(files_list) if len(file) <= l.count(-1)]

        if free:
            suitable_space = free[0]
            index_start = suitable_space[1].index(-1)
            suitable_space[1][index_start : index_start + len(file)] = file
            files_list[suitable_space[0]] = suitable_space[1]
            last_index = len(files_list) - 1 - files_list[::-1].index(file)
            files_list[last_index] = [-1] * len(file)

    flattened_list = [
        int(item) if item != -1 else 0 for file in files_list for item in file
    ]
    checksum = [i * x for i, x in enumerate(flattened_list)]
    return sum(checksum)


res_example = main("2024/day09_example.txt")
print(res_example)
res_example = main("2024/day09_example1.txt")
print(res_example)
res_example = main("2024/day09_example2.txt")
print(res_example)
res_actual = main("2024/day09_input.txt")
print(res_actual)
