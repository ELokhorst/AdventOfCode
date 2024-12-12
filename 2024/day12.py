def find_regions(coord_set: set):
    regions = []
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    while coord_set:
        x, y, char = coord_set.pop()
        region = [(x, y, char)]
        stack = [(x, y, char)]

        while stack:
            cx, cy, cchar = stack.pop()
            for dx, dy in directions:
                neighbor = (cx + dx, cy + dy, cchar)
                if neighbor in coord_set:
                    coord_set.remove(neighbor)
                    stack.append(neighbor)
                    region.append(neighbor)

        regions.append(region)

    return regions


def count_surrounding_lots(lot, coord):
    x, y, char = coord
    p = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    res = sum([(x + dx, y + dy, char) not in lot for dx, dy in p])
    return res


def main(file: str):
    with open(file, "r", encoding="utf-8") as f:
        layout = f.read().strip()

    lines = layout.splitlines()
    coords = set()
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            coords.add((x, y, char))

    regions = find_regions(coords)

    sizes = [len(lots) for lots in regions]
    perimeters = [
        sum(count_surrounding_lots(lots, coord) for coord in lots) for lots in regions
    ]
    costs = [a * b for a, b in zip(sizes, perimeters)]
    return sum(costs)


res_example = main("2024/day12_example.txt")
print(res_example)
res_actual = main("2024/day12_input.txt")
print(res_actual)
