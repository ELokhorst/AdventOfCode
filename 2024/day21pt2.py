## Solution thanks to Sanvirk99: https://github.com/sanvirk99/adventcode/blob/main/day21recursion.py

from collections import defaultdict
from itertools import permutations

numPad = [["7", "8", "9"], ["4", "5", "6"], ["1", "2", "3"], ["#", "0", "A"]]

dirPad = [["#", "^", "A"], ["<", "v", ">"]]

moveSpace = []
for i in range(-3, 4):
    for j in range(-2, 3):
        if abs(i) in range(0, 4) and abs(j) in range(0, 3):
            moveSpace.append((i, j))

dirSpace = []
for i in range(-1, 2):
    for j in range(-2, 3):
        if abs(i) in range(0, 2) and abs(j) in range(0, 3):
            dirSpace.append((i, j))


# change this symboling reflect move length
def symbolx(x):
    if x < 0:
        return "^" * abs(x)
    if x > 0:
        return "v" * abs(x)
    return ""


def symboly(y):
    if y < 0:
        return "<" * abs(y)
    if y > 0:
        return ">" * abs(y)
    return ""


directions = {"^": (-1, 0), "v": (1, 0), "<": (0, -1), ">": (0, 1)}


def validate(grid, cur, end, seq):
    def dfs(cur, k):
        x, y = cur
        if cur == end:
            return True
        if grid[x][y] == "#":
            return False
        px, py = directions[seq[k]]
        return dfs((x + px, y + py), k + 1)

    return dfs(cur, 0)


numMoves = defaultdict(defaultdict)
for i, line in enumerate(numPad):
    for j, char in enumerate(line):
        if numPad[i][j] == "#":
            continue
        for move in moveSpace:
            dx, dy = move
            nx, ny = i + dx, j + dy
            if (
                nx in range(len(numPad))
                and ny in range(len(numPad[0]))
                and numPad[nx][ny] != "#"
            ):
                seq1 = symbolx(dx) + symboly(dy)
                perm = list(permutations(seq1))
                unique = set()
                for p in perm:

                    if validate(numPad, (i, j), (nx, ny), "".join(p)):
                        temp = list(p)
                        temp.append("A")
                        unique.add("".join(temp))
                numMoves[numPad[i][j]][numPad[nx][ny]] = unique

dirMoves = defaultdict(dict)
for i, line in enumerate(dirPad):
    for j, char in enumerate(line):
        if dirPad[i][j] == "#":
            continue
        for move in dirSpace:
            dx, dy = move
            nx, ny = i + dx, j + dy
            if (
                nx in range(len(dirPad))
                and ny in range(len(dirPad[0]))
                and dirPad[nx][ny] != "#"
            ):
                seq1 = symbolx(dx) + symboly(dy)
                perm = list(permutations(seq1))
                unique = set()
                for p in perm:
                    if validate(dirPad, (i, j), (nx, ny), "".join(p)):
                        temp = list(p)
                        if not temp:
                            temp = ["A"]
                        else:
                            temp.append("A")
                        # print(print(temp),'dir')
                        unique.add("".join(temp))

                dirMoves[dirPad[i][j]][dirPad[nx][ny]] = unique


def allcombination(totype):
    res = []

    def dfs(totype, combo, from_):
        if len(totype) == 0:
            res.append(combo)
            return
        for cmove in numMoves[from_][totype[0]]:
            choice = combo + cmove
            dfs(totype[1:], choice, totype[0])

    dfs(totype, "", "A")
    return res


def dircombinations(totype):
    res = []

    def dfs(totype, combo, from_):
        if len(totype) == 0:
            res.append(combo)
            return
        for cmove in dirMoves[from_][totype[0]]:
            choice = combo + cmove
            dfs(totype[1:], choice, totype[0])

    dfs(totype, "", "A")
    return res


def chainRobot(letter, prev, end, seqstart):
    memo = {}

    def dfs(letter, prev, ii, start):
        if ii == end:
            return 1
        if (letter, prev, ii, start) in memo:
            return memo[(letter, prev, ii, start)]
        mincount = float("inf")
        if start:
            prev = "A"
        for cmove in dirMoves[prev][letter]:
            count = 0
            cur = prev
            begin = True
            for each in cmove:
                count += dfs(each, cur, ii + 1, begin)
                begin = False
                cur = each
            if count < mincount:
                mincount = min(mincount, count)
        memo[(letter, prev, ii, start)] = mincount
        return mincount

    return dfs(letter, prev, 0, seqstart)


def vtype(totype, depth):
    combinations = allcombination(totype)
    minlen = float("inf")
    for seq in combinations:
        prev = "A"
        start = True
        res = 0
        for letter in seq:
            res += chainRobot(letter, prev, depth, start)
            start = False
            prev = letter
        minlen = min(res, minlen)
    return minlen * int(totype[:-1])


def part2():
    count = 0
    with open("2024/day21_input.txt", "r", encoding="utf-8") as f:
        lines = f.read().strip().splitlines()
    count = sum([vtype(line, 25) for line in lines])
    print("input depth 25 ", count)


part2()
