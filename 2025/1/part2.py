def parse_rotation(r):
    if r.startswith('R'):
        return int(r[1:])
    return -1 * int(r[1:])

def parse_input():
    with open("input.txt") as f:
        rotations = [parse_rotation(r) for r in f.read().splitlines()]
    return rotations

def get_password(rotations):
    current = 50
    password = 0
    for r in rotations:
        if r == 0:
            continue
        elif r < 0 and current + r <= 0:
            password += (1 if current > 0 else 0) + abs(current + r) // 100
        elif r > 0 and current + r >= 100:
            password += (current + r) // 100
        current = (current + r) % 100
    return password

def solution():
    rotations = parse_input()
    password = get_password(rotations)
    print(password)

if __name__ == "__main__":
    solution()
