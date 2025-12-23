def parse_rotation(r):
    if r.startswith('R'):
        return int(r[1:])
    return -1 * int(r[1:])

def parse_input():
    with open("input.txt") as f:
        rotations = [parse_rotation(r) for r in f.read().splitlines()]
    return rotations

def solution():
    rotations = parse_input()
    current = 50
    password = 0
    for r in rotations:
        current = (current + r) % 100
        if current == 0:
            password += 1
    print(password)

if __name__ == "__main__":
    solution()
