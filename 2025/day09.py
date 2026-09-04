from itertools import combinations
from typing import Tuple

Point = Tuple[int, int]


def inside(poly, x, y):
    """Point inside polygon (ray casting)."""
    result = False

    for (x1, y1), (x2, y2) in zip(poly, poly[1:] + poly[:1]):
        if (y1 > y) != (y2 > y):
            hit = x1 + (y - y1) * (x2 - x1) / (y2 - y1)
            if hit > x:
                result = not result

    return result


def valid_rect(poly, a, b):
    x1, x2 = sorted((a[0], b[0]))
    y1, y2 = sorted((a[1], b[1]))

    # A point in the rectangle's interior.
    if x1 != x2 and y1 != y2:
        if not inside(poly, (x1 + x2) / 2, (y1 + y2) / 2):
            return False

    # Make sure no polygon edge crosses the rectangle interior.
    for (ax, ay), (bx, by) in zip(poly, poly[1:] + poly[:1]):
        if ax == bx:
            if x1 < ax < x2:
                ey1, ey2 = sorted((ay, by))
                if max(y1, ey1) < min(y2, ey2):
                    return False

        elif y1 < ay < y2:
            ex1, ex2 = sorted((ax, bx))
            if max(x1, ex1) < min(x2, ex2):
                return False

    return True


def part2(file):
    with open(file, "r", encoding="utf-8") as f:
        points = [tuple(map(int, line.split(","))) for line in f if line.strip()]

    best = 0

    for a, b in combinations(points, 2):
        area = (abs(a[0] - b[0]) + 1) * (abs(a[1] - b[1]) + 1)

        if area <= best:
            continue

        if valid_rect(points, a, b):
            best = area

    return best


def part1(file: str):
    with open(file, "r", encoding="utf-8") as f:
        lines = f.read().splitlines()

    max_area = 0
    coords = [tuple(map(int, line.split(","))) for line in lines]
    for A, B in combinations(coords, 2):
        ax, ay = A
        bx, by = B

        width = abs(ax - bx) + 1
        height = abs(ay - by) + 1
        max_area = max(max_area, width * height)
    return max_area


res_example = part1("2025/day09_example.txt")
print(res_example)
res_actual = part1("2025/day09_input.txt")
print(res_actual)

res_example = part2("2025/day09_example.txt")
print(res_example)
res_actual = part2("2025/day09_input.txt")
print(res_actual)
