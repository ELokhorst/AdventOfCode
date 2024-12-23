from collections import defaultdict as dd


def find_cycles(nodes: set, graph: set):
    cycles = set()
    visited = set()

    def dfs(node, parent, path: list):
        if len(path) >= 3:
            return
        path.append(node)
        for neighbor in graph[node]:
            if neighbor == parent:
                continue
            if neighbor in path:
                cycle_start_index = path.index(neighbor)
                cycle = tuple(sorted(path[cycle_start_index:]))
                cycles.add(cycle)
                continue
            if neighbor not in visited:
                dfs(neighbor, node, path)
        path.pop()

    for node in nodes:
        dfs(node, None, [])
        visited.add(node)

    return [list(cycle) for cycle in cycles]


def main(file: str):
    with open(file, "r", encoding="utf-8") as f:
        lines = f.read().strip().splitlines()

    connections = [line.split("-") for line in lines]
    computers = set(
        pc for connection in connections for pc in connection if pc.startswith("t")
    )
    graph = dd(set)
    for pc1, pc2 in connections:
        graph[pc1].add(pc2)
        graph[pc2].add(pc1)

    groups = find_cycles(computers, graph)
    return len(groups)


res_example = main("2024/day23_example.txt")
print(res_example)
res_actual = main("2024/day23_input.txt")
print(res_actual)
