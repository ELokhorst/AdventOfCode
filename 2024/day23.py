from collections import defaultdict as dd
from itertools import combinations


def bron_kerbosch(r, p, x, graph, cliques):
    if not p and not x:
        cliques.add(tuple(sorted(r)))  # Found a maximal clique
        return

    for vertex in list(p):
        new_r = r.union({vertex})
        new_p = p.intersection(graph[vertex])
        new_x = x.intersection(graph[vertex])
        bron_kerbosch(new_r, new_p, new_x, graph, cliques)
        p.remove(vertex)
        x.add(vertex)


def find_maximal_cliques(graph):
    cliques = set()
    bron_kerbosch(set(), set(graph.keys()), set(), graph, cliques)
    return cliques


def main(file: str):
    with open(file, "r", encoding="utf-8") as f:
        lines = f.read().strip().splitlines()

    connections = [line.split("-") for line in lines]
    graph = dd(set)
    for pc1, pc2 in connections:
        graph[pc1].add(pc2)
        graph[pc2].add(pc1)

    cycles = find_maximal_cliques(graph)  # part 2

    visited = set()
    part1 = 0
    for cycle in cycles:
        if len(cycle) >= 3:
            for comb in combinations(cycle, 3):
                if any(c.startswith("t") for c in comb) and comb not in visited:
                    part1 += 1
                    visited.add(comb)
    print(part1)

    result = ",".join(sorted(max(cycles, key=len)))
    return result


res_example = main("2024/day23_example.txt")
print(res_example)
res_actual = main("2024/day23_input.txt")
print(res_actual)
