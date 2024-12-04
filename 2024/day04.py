from collections import Counter


def find_occurrences(grid, target_char):
    occurrences = [
        (i, j)
        for i in range(len(grid))
        for j in range(len(grid[i]))
        if grid[i][j] == target_char
    ]
    return occurrences


def find_adjacent(list1, list2, list3):
    offsets = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
    set2 = set(list2)
    set3 = set(list3)

    a_coords = []
    for coord in list1:
        for offset in offsets:
            adjacent_coord = (coord[0] + offset[0], coord[1] + offset[1])
            if adjacent_coord in set2:
                a_coord = adjacent_coord  # added for part 2
                adjacent_coord = (
                    adjacent_coord[0] + offset[0],
                    adjacent_coord[1] + offset[1],
                )
                if adjacent_coord in set3:
                    a_coords.append(a_coord)

    count = Counter(a_coords)
    xmas = 0
    for coord, cnt in count.items():
        if cnt > 1:
            xmas += 1
    return xmas


def day4_func(file: str):
    with open(file, "r", encoding="utf-8") as f:
        lines = f.readlines()

    # occurences_X = find_occurrences(lines, "X")
    occurences_M = find_occurrences(lines, "M")
    occurences_A = find_occurrences(lines, "A")
    occurences_S = find_occurrences(lines, "S")

    xmas = find_adjacent(occurences_M, occurences_A, occurences_S)

    return xmas


res_example = day4_func("2024/day04_example.txt")
print(res_example)
res_actual = day4_func("2024/day04_input.txt")
print(res_actual)
