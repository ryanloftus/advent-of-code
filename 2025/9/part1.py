def parse_input():
    with open("input.txt") as f:
        return [[int(x) for x in line.split(",")] for line in f.read().splitlines()]

def area(t1, t2):
    l = max(t1[0], t2[0]) - min(t1[0], t2[0]) + 1
    w = max(t1[1], t2[1]) - min(t1[1], t2[1]) + 1
    return l * w

def solution():
    red_tiles = parse_input()
    max_area = 0
    for i in range(len(red_tiles)):
        for j in range(i+1, len(red_tiles)):
            max_area = max(max_area, area(red_tiles[i], red_tiles[j]))
    print(max_area)

if __name__ == "__main__":
    solution()
