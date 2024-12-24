def main(file: str):
    with open(file, "r", encoding="utf-8") as f:
        content = f.read().strip().split("\n\n")

    states = {
        k: int(v) for line in content[0].splitlines() for k, v in [line.split(": ")]
    }
    rules = [
        [item[1], item[0], item[2], item[4]]
        for line in content[1].splitlines()
        for item in [line.split()]
    ]
    for rule in rules:
        if rule[-1].startswith("z"):
            states[rule[-1]] = -1

    while True:
        next_states = states.copy()
        for rule in rules:
            if rule[1] not in states or rule[2] not in states:
                continue
            match (rule[0]):
                case "AND":
                    next_states[rule[-1]] = states[rule[1]] and states[rule[2]]
                case "OR":
                    next_states[rule[-1]] = states[rule[1]] or states[rule[2]]
                case "XOR":
                    next_states[rule[-1]] = states[rule[1]] ^ states[rule[2]]
        states = next_states

        if all(v > -1 for k, v in states.items() if k.startswith("z")):
            break

    output_bits = "".join(
        [str(v) for k, v in sorted(states.items()) if k.startswith("z")][::-1]
    )
    return states, int(output_bits, 2)


res_example = main("2024/day24_example.txt")
print(res_example)
res_actual = main("2024/day24_input.txt")
print(res_actual)
