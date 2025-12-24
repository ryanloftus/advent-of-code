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

def remove_maximal_rolls(grid):
    while True:
        mgrid = [[c for c in row] for row in grid]
        changed = False
        for y in range(len(grid)):
            for x in range(len(grid[y])):
                if mgrid[y][x] == "@" and can_access(mgrid, x, y):
                    mgrid[y][x] = "x"
                    changed = True
        if not changed:
            return mgrid
        grid = mgrid

def count_removed_rolls(grid):
    count = 0
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == "x":
                count += 1
    return count

def solution():
    grid = parse_input()
    final_grid = remove_maximal_rolls(grid)
    removed_rolls = count_removed_rolls(final_grid)
    print(removed_rolls)

if __name__ == "__main__":
    solution()