def mix(secretno: int, givenval: int):
    return secretno ^ givenval


def prune(secretno: int):
    return secretno % 16777216


def calc_next_secret(n: int):
    # Step 1
    n = prune(mix(n, n * 64))
    # Step 2
    n = prune(mix(n, n // 32))
    # Step 3
    n = prune(mix(n, n * 2048))
    return n


def generate_secrets(tracker: dict, target: int, initial_value: int):
    secrets = []
    created = 0

    nv = initial_value
    while created < target:
        if nv in tracker:
            nv = tracker[nv]
            secrets.append(nv)
        else:
            tracker[nv] = calc_next_secret(nv)
            nv = tracker[nv]
            secrets.append(nv)
        created += 1

    return secrets


def main(file: str):
    with open(file, "r", encoding="utf-8") as f:
        lines = f.read().strip().splitlines()

    numbers = [int(line) for line in lines]
    secrets_per_number = []
    tracker = {}
    target = 2000
    for n in numbers:
        secrets = generate_secrets(tracker, target, n)
        secrets_per_number.append(secrets)

    lastnum = [l[-1] for l in secrets_per_number]
    return sum(lastnum)


res_example = main("2024/day22_example.txt")
print(res_example)
res_actual = main("2024/day22_input.txt")
print(res_actual)
