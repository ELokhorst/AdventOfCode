def main(file: str):
    with open(file, "r", encoding="utf-8") as f:
        disk = f.read().strip()

    files = [(id, size) for id, size in enumerate(map(int, disk[::2]))]
    free = list(map(int, disk[1::2]))
    file_string = [file[1] * str(file[0]) for file in files]
    print(file_string)

    moved_fb = []
    for i, size in enumerate(free):
        if len(file_string) <= size:
            while file_string:
                moved_fb.append(file_string.pop())

        if not file_string:
            break
        moved_fb.extend(files[i][1] * str(files[i][0]))
        file_string = file_string[files[i][1] :]
        for _ in range(size):
            if file_string:
                moved_fb.append(file_string.pop())

    checksum = sum([i * int(item) for i, item in enumerate(moved_fb)])
    return checksum


res_example = main("2024/day09_example.txt")
print(res_example)
# res_actual = main("2024/day09_input.txt")
# print(res_actual)
