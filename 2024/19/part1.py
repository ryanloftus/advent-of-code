def parse_input():
    with open("input.txt") as f:
        lines = f.read().splitlines()
        available_towels = lines[0].split(", ")
        desired_pattens = lines[2:]
        return set(available_towels), desired_pattens

def is_possible(available_towels, pattern):
    dp = [False] * (len(pattern) + 1)
    dp[0] = True
    for i in range(1, len(dp)):
        for j in range(i):
            if dp[j] and pattern[j:i] in available_towels:
                dp[i] = True
                break
    return dp[-1]

def count_possible(available_towels, desired_patterns):
    count = 0
    for pattern in desired_patterns:
        if is_possible(available_towels, pattern):
            count += 1
    return count

def solution():
    available_towels, desired_patterns = parse_input()
    num_possible = count_possible(available_towels, desired_patterns)
    print(num_possible)

if __name__ == "__main__":
    solution()
