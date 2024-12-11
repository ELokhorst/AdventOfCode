import math


def process_stone(stone):
    """Yield the resulting stones without creating a full list."""
    if stone == 0:
        return [1]
    else:
        num_digits = int(math.log10(abs(stone))) + 1
        if num_digits % 2 == 1:
            return [stone * 2024]
        else:
            mid_index = num_digits // 2
            divisor = 10**mid_index
            return [stone // divisor, stone % divisor]


def update_stones(stone_piles: dict, stone: int, stones_to_add: int = 1):
    if stone_piles.get(stone, None) is None:
        stone_piles[stone] = stones_to_add
    else:
        stone_piles[stone] += stones_to_add


def main(file: str):
    with open(file, "r", encoding="utf-8") as f:
        stones = f.read().strip().split(" ")

    stones = list(map(int, stones))
    blinks = 6
    stone_piles = {}
    # Credits to https://github.com/ambrosekuo/aoc-2024/blob/main/aoc-python%2Fday11%2Fmain2.py
    # For this efficiency improvement that I needed for part 2
    # All numbers are accumulated, so each computation only needs to happen once!
    for stone in stones:
        update_stones(stone_piles, stone)

    current_blink = 0
    while current_blink < blinks:
        new_piles = {}
        for key, count in stone_piles.items():
            new_stones = process_stone(key)
            update_stones(new_piles, new_stones[0], count)
            if len(new_stones) == 2:
                update_stones(new_piles, new_stones[1], count)
        stone_piles = new_piles
        current_blink += 1

    total_len = sum([count for count in stone_piles.values()])
    return total_len


res_example = main("2024/day11_example.txt")
print(res_example)
# res_actual = main("2024/day11_input.txt")
# print(res_actual)
