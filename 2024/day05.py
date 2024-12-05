from collections import defaultdict, deque


def topological_sort(instruction_dict):
    graph = defaultdict(list)
    in_degree = defaultdict(int)

    for key, values in instruction_dict.items():
        for value in values:
            graph[value].append(key)
            in_degree[key] += 1
            if value not in in_degree:
                in_degree[value] = 0
    queue = deque([node for node in in_degree if in_degree[node] == 0])

    result = []
    while queue:
        current = queue.popleft()
        result.append(current)

        for neighbor in graph[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    if len(result) != len(in_degree):
        raise ValueError("A cycle was detected in the graph; ordering is not possible.")

    return result


def verify_order(ordering: list, ruleset: defaultdict[int, list]):
    for k, v in ruleset.items():
        if k in ordering:
            pos = ordering.index(k)
            selected_order = ordering[pos:]
            for num in v:
                if num in set(selected_order):
                    print(f"Found {num} after {k} in {ordering}")
                    return 0
    return ordering[len(ordering) // 2]


def restructure_order(ordering: list, ruleset: defaultdict[int, list]):
    rules_filtered = defaultdict(list)
    for key in ruleset:
        if key in ordering:
            rules_filtered[key] = ruleset[key]
    topo_sort = topological_sort(rules_filtered)

    order_map = {value: index for index, value in enumerate(topo_sort)}
    sorted_list = sorted(ordering, key=lambda x: order_map.get(x, float("inf")))

    return sorted_list


def main(file: str):
    with open(file, "r", encoding="utf-8") as f:
        content = f.read()

    rules, orderings = content.split("\n\n")
    rules = rules.split("\n")
    orderings = [list(map(int, order.split(","))) for order in orderings.split("\n")]

    agg_rules: defaultdict[int, list] = defaultdict(list)
    for rule in rules:
        number, key = map(int, rule.split("|"))
        agg_rules[key].append(number)

    wrong_orderings = [
        order for order in orderings if verify_order(order, agg_rules) == 0
    ]

    corrected = [restructure_order(order, agg_rules) for order in wrong_orderings]
    result = sum([verify_order(order, agg_rules) for order in corrected])

    return result


res_example = main("2024/day05_example.txt")
print(res_example)
res_actual = main("2024/day05_input.txt")
print(res_actual)
