def parse_input():
    with open("input.txt") as f:
        return f.read().splitlines()

DIRECTIONS = {
    (1, 0),
    (0, 1),
    (-1, 0),
    (0, -1),
    (1, 1),
    (1, -1),
    (-1, 1),
    (-1, -1)
}

def can_access(grid, x, y):
    nearby_rolls = 0
    for dx, dy in DIRECTIONS:
        xp, yp = x+dx, y+dy
        if yp >= 0 and yp < len(grid) and xp >= 0 and xp < len(grid[yp]) and grid[yp][xp] == "@":
            nearby_rolls += 1
    return nearby_rolls < 4

def solution():
    grid = parse_input()
    accessible_rolls = 0
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == "@" and can_access(grid, x, y):
                accessible_rolls += 1
    print(accessible_rolls)

if __name__ == "__main__":
    solution()