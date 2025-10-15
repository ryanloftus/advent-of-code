from collections import deque

p = 16777216

def parse_input():
    with open("input.txt") as f:
        return [int(x) for x in f.read().splitlines()]

def mix(secret, value):
    return secret ^ value

def prune(secret):
    return secret % p

def next_secret(secret):
    secret = prune(mix(secret, secret * 64))
    secret = prune(mix(secret, secret // 32))
    secret = prune(mix(secret, secret * 2048))
    return secret

def get_sequence_to_price_mapping(secret):
    mapping = dict()
    prev = deque()
    prev.append((secret % 10, 0))
    for i in range(2000):
        secret = next_secret(secret)
        price = secret % 10
        prev.append((price, price-prev[-1][0]))
        if len(prev) == 5:
            prev.popleft()
            seq = tuple(p[1] for p in prev)
            if seq not in mapping:
                mapping[seq] = price
    return mapping

def solution():
    initial_secrets = parse_input()
    seq_to_price_mappings = [get_sequence_to_price_mapping(s) for s in initial_secrets]
    max_bananas = 0
    for i in range(-9, 10):
        i_min_val = max(0, 0+i)
        i_max_val = min(9, 9+i)
        for j in range(-i_max_val, 10-i_min_val):
            j_min_val = max(0, i_min_val + j)
            j_max_val = min(9, i_max_val + j)
            for k in range(-j_max_val, 10-j_min_val):
                k_min_val = max(0, j_min_val + k)
                k_max_val = min(9, j_max_val + k)
                for l in range(-k_max_val, 10-k_min_val):
                    max_bananas = max(max_bananas, sum(seq_to_price.get((i, j, k, l), 0) for seq_to_price in seq_to_price_mappings))
    print(max_bananas)

if __name__ == "__main__":
    solution()
