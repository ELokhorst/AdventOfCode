from collections import Counter


def main(file: str):
    with open(file, "r", encoding="utf-8") as f:
        disk = f.read().strip()

    files = [(id, size) for id, size in enumerate(map(int, disk[::2]))]
    free = list(map(int, disk[1::2]))
    files_list = [int(x) for file in files for x in file[1] * [file[0]]]

    new_order = []
    for i, size in enumerate(free):
        if len(files_list) > size:
            new_order.extend(min(files[i][1], len(files_list)) * [files[i][0]])
            files_list = files_list[files[i][1] :]

            for _ in range(size):
                if files_list:
                    new_order.append(files_list.pop())
        else:
            while files_list:
                new_order.append(files_list.pop())

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
