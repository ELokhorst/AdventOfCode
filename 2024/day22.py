def mix(secretno: int, givenval: int):
    return secretno ^ givenval


def prune(secretno: int):
    return secretno % 16777216


def calc_next_secret(n: int):
    n = prune(mix(n, n * 64))
    n = prune(mix(n, n // 32))
    n = prune(mix(n, n * 2048))
    return n


def generate_secrets(tracker: dict, target: int, initial_value: int):
    secrets = []
    created = 0

    nv = initial_value
    while created < target:
        if nv in tracker:
            nv = tracker[nv]
        else:
            tracker[nv] = calc_next_secret(nv)
            nv = tracker[nv]
        secrets.append(nv)
        created += 1

    return secrets


def add_sequence(sequences: dict, sublists: list[tuple], prices):
    seen = set()
    for tupl, price in zip(sublists, prices):
        if tupl not in seen:
            seen.add(tupl)
            if tupl not in sequences:
                sequences[tupl] = price
            else:
                sequences[tupl] += price


def main(file: str):
    with open(file, "r", encoding="utf-8") as f:
        lines = f.read().strip().splitlines()

    buyers = [int(line) for line in lines]
    secrets_per_number = []
    tracker = {}
    target = 2000
    for buyer in buyers:
        secrets = generate_secrets(tracker, target, buyer)
        secrets_per_number.append(secrets)

    sequences = {}
    for buyer in buyers:
        secrets = generate_secrets(tracker, target, buyer)
        prices = [secret % 10 for secret in secrets]
        diffs = [prices[i + 1] - prices[i] for i in range(len(prices) - 1)]
        sublists = [tuple(diffs[i - 4 : i]) for i in range(4, len(diffs))]
        add_sequence(sequences, sublists, prices[4:])

    best_sequence = max(sequences.items(), key=lambda x: x[1])

    lastnum = sum([l[-1] for l in secrets_per_number])  # Part 1
    return lastnum, best_sequence


res_example = main("2024/day22_example.txt")
print(res_example)
res_actual = main("2024/day22_input.txt")
print(res_actual)
