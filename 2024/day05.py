from collections import defaultdict


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


def restructure_order(ordering: list, rules: list):
    reordered_list = []
    added = set()

    for item in rules:
        if item in ordering and item not in added:
            reordered_list.append(item)
            added.add(item)

    for item in ordering:
        if item not in added:
            reordered_list.append(item)

    return reordered_list


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
