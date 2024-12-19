def is_partition_possible(s: str, patterns: set) -> int:
    def count_partitions(start, memo):
        if start == len(s):
            return 1
        if start in memo:
            return memo[start]

        total_count = 0
        for end in range(start + 1, len(s) + 1):
            substring = s[start:end]
            if substring in patterns:
                total_count += count_partitions(end, memo)

        memo[start] = total_count
        return total_count

    memo = {}
    return count_partitions(0, memo)


def main(file: str):
    with open(file, "r", encoding="utf-8") as f:
        lines = f.read().strip().split("\n\n")

    patterns = set(lines[0].split(", "))
    requests = [line.strip() for line in lines[1].splitlines()]

    correct = 0
    for request in requests:
        print(request)
        correct += is_partition_possible(request, patterns)

    return correct


res_example = main("2024/day19_example.txt")
print(res_example)
res_actual = main("2024/day19_input.txt")
print(res_actual)
