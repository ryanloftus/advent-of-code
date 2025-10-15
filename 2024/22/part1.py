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

def get_2000th_secret(secret):
    for i in range(2000):
        secret = next_secret(secret)
    return secret

def solution():
    initial_secrets = parse_input()
    final_secrets = [get_2000th_secret(s) for s in initial_secrets]
    print(sum(final_secrets))

if __name__ == "__main__":
    solution()
