def count_surrounding_lots(lot, coord):
    x, y, char = coord
    p = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    res = sum([(x + dx, y + dy, char) not in lot for dx, dy in p])
    return res


def main(file: str):
    with open(file, "r", encoding="utf-8") as f:
        layout = f.read().strip()

    lines = layout.splitlines()
    coords = []
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            coords.append((x, y, char))

    visited = set()
    regions = []
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    while coords:
        x, y, char = coords[0]
        if (x, y, char) in visited:
            continue
        visited.add((x, y, char))
        coords.remove((x, y, char))

        region = [(x, y, char)]
        found_region = True
        while found_region is True:
            found_region = False
            for x, y, char in region:
                for d in directions:
                    new_pos = (x + d[0], y + d[1], char)
                    if new_pos in coords:
                        region += [new_pos]
                        coords.remove(new_pos)
                        found_region = True

        regions.append(region)
    print(regions)

    sizes = [len(lots) for lots in regions]
    print(sizes)
    perimeters = [
        sum(count_surrounding_lots(lots, coord) for coord in lots) for lots in regions
    ]
    print(perimeters)
    costs = [a * b for a, b in zip(sizes, perimeters)]
    return sum(costs)


res_example = main("2024/day12_example.txt")
print(res_example)
res_actual = main("2024/day12_input.txt")
print(res_actual)
