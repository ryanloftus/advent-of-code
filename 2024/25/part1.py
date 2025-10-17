def is_lock(schematic):
    return schematic[0] == "#####"

def parse_lock(schematic):
    heights = [0] * 5
    for col in range(5):
        for row in range(7):
            if schematic[row][col] == "#":
                heights[col] = row
    return tuple(heights)

def parse_key(schematic):
    heights = [0] * 5
    for col in range(5):
        for row in range(6, -1, -1):
            if schematic[row][col] == "#":
                heights[col] = 6-row
    return tuple(heights)

def parse_input():
    locks = set()
    keys = set()
    with open("input.txt") as f:
        lines = f.read().splitlines()
        for i in range(0, len(lines), 8):
            schematic = lines[i:i+7]
            if is_lock(schematic):
                locks.add(parse_lock(schematic))
            else:
                keys.add(parse_key(schematic))
    return locks, keys

def is_match(lock, key):
    for i in range(5):
        if lock[i] + key[i] > 5:
            return False
    return True

def find_matches(locks, keys):
    matches = 0
    for key in keys:
        for lock in locks:
            if is_match(lock, key):
                matches += 1
    return matches

def solution():
    locks, keys = parse_input()
    num_matches = find_matches(locks, keys)
    print(num_matches)

if __name__ == "__main__":
    solution()
