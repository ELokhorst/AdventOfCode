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


def restructure_order(ordering: list, ruleset: defaultdict[int, list]):
    reordered_list = []

    for number in ordering:
        print(f"Starting number: {number}")
        current_val = number
        rules = ruleset[number]

        while len(rules) > 0:
            i = 0
            while (
                i < len(rules)
                and rules[i] in ordering
                and rules[i] not in reordered_list
            ):
                print(rules[i])
                current_val = rules[i]
                rules = ruleset[rules[i]]
                print(f"{current_val}: {rules}")
                i += 1

            if current_val not in reordered_list and current_val > 0:
                reordered_list.insert(0, current_val)
                print(f"List: {reordered_list}")
            break

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

    print(agg_rules)
    corrected = [restructure_order(order, agg_rules) for order in wrong_orderings]
    result = sum([verify_order(order, agg_rules) for order in corrected])

    return result


res_example = main("2024/day05_example.txt")
print(res_example)
# res_actual = main("2024/day05_input.txt")
# print(res_actual)
