def find_regions(coord_set: set):
    regions = []
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    while coord_set:
        x, y, char = coord_set.pop()
        region = set()
        region.add((x, y))
        stack = [(x, y, char)]

        while stack:
            cx, cy, cchar = stack.pop()
            for dx, dy in directions:
                neighbor = (cx + dx, cy + dy, cchar)
                if neighbor in coord_set:
                    coord_set.remove(neighbor)
                    stack.append(neighbor)
                    region.add((neighbor[0], neighbor[1]))

        regions.append(region)

    return regions


def count_surrounding_lots(lot, coord):
    x, y, char = coord
    p = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    res = sum([(x + dx, y + dy, char) not in lot for dx, dy in p])
    return res


# Credits to Boojum (reddit) for this solution of counting corners!
def count_corners(region: set):
    if len(region) < 3:
        return 4

    corners = 0
    for x, y in region:
        # Outer corners
        corners += (x - 1, y) not in region and (
            x,
            y - 1,
        ) not in region  # left top corner
        corners += (x + 1, y) not in region and (
            x,
            y - 1,
        ) not in region  # right top corner
        corners += (x - 1, y) not in region and (
            x,
            y + 1,
        ) not in region  # left bottom corner
        corners += (x + 1, y) not in region and (
            x,
            y + 1,
        ) not in region  # right bottom corner
        # Inner corners
        corners += (
            (x - 1, y) in region
            and (x, y - 1) in region
            and (x - 1, y - 1) not in region
        )
        corners += (
            (x + 1, y) in region
            and (x, y - 1) in region
            and (x + 1, y - 1) not in region
        )
        corners += (
            (x - 1, y) in region
            and (x, y + 1) in region
            and (x - 1, y + 1) not in region
        )
        corners += (
            (x + 1, y) in region
            and (x, y + 1) in region
            and (x + 1, y + 1) not in region
        )

    return corners


def main(file: str):
    with open(file, "r", encoding="utf-8") as f:
        layout = f.read().strip()

    lines = layout.splitlines()
    coords = set()
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            coords.add((x, y, char))

    regions = find_regions(coords)
    edges = [count_corners(region) for region in regions]

    sizes = [len(lots) for lots in regions]
    # perimeters = [
    #     sum(count_surrounding_lots(lots, coord) for coord in lots) for lots in regions
    # ]
    # costs = [a * b for a, b in zip(sizes, perimeters)]
    costs = [a * b for a, b in zip(sizes, edges)]
    return sum(costs)


res_example = main("2024/day12_example.txt")
print(res_example)
res_actual = main("2024/day12_input.txt")
print(res_actual)
