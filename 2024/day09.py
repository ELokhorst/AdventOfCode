def main(file: str):
    with open(file, "r", encoding="utf-8") as f:
        disk = f.read().strip()

    files = [(id, size) for id, size in enumerate(map(int, disk[::2]))]
    free = [(id, size) for id, size in enumerate(list(map(int, disk[1::2])))]
    files_list = [file[1] * [file[0]] for file in files]
    print(files_list)
    files_list.reverse()

    new_order = [files_list[-1]]
    stack = []
    for file in files_list[:-1]:
        print(f"File: {file}")

        suitable_space = None
        for index, size in free:
            if len(file) <= size:
                suitable_space = (index, size)
                break
        print(suitable_space)

        if suitable_space:
            remaining_space = suitable_space[1] - len(file)
            free[suitable_space[0]] = (
                suitable_space[0] + 1,
                remaining_space,
            )
            files_list.remove(file)
            new_order.insert(suitable_space[0] + 1, file)
        else:
            stack.append(file)
        print(new_order)

    for file in stack:
        new_order.append(file)
    print(new_order)

    print(free)
    for idx, space in free:
        new_order.insert(idx + 2, [0] * space)
    print(new_order)

    checksum = [i * int(item) for i, item in enumerate(new_order)]
    return sum(checksum)


res_example = main("2024/day09_example.txt")
print(res_example)
res_example = main("2024/day09_example1.txt")
print(res_example)
res_example = main("2024/day09_example2.txt")
print(res_example)
res_actual = main("2024/day09_input.txt")
print(res_actual)
