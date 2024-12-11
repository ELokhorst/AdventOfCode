def main(file: str):
    with open(file, "r", encoding="utf-8") as f:
        stones = f.read().strip().split(" ")

    stones = list(map(int, stones))
    blinks = 25
    for _ in range(blinks):
        new_list = []
        for stone in stones:
            stone_str = str(stone)
            if stone == 0:
                new_list.append(1)
            elif len(stone_str) % 2 == 0:
                mid_index = len(stone_str) // 2
                stone1 = int(stone_str[:mid_index])
                stone2 = int(stone_str[mid_index:])
                new_list.extend([stone1, stone2])
            else:
                new_list.append(stone * 2024)
        stones = new_list
    return len(stones)


res_example = main("2024/day11_example.txt")
print(res_example)
res_actual = main("2024/day11_input.txt")
print(res_actual)
