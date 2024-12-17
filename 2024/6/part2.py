def find_guard_location(grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "^":
                return i, j
    raise "security guard not found!"

def is_loop(grid, si, sj):
    i = si
    j = sj
    di = -1
    dj = 0
    visited = set()
    while (i, j, di, dj) not in visited:
        visited.add((i, j, di, dj))
        if i+di < 0 or i+di >= len(grid) or j+dj < 0 or j+dj >= len(grid[i]):
            return False
        elif grid[i+di][j+dj] != "#":
            i += di
            j += dj
        else:
            if di == -1:
                di = 0
                dj = 1
            elif di == 1:
                di = 0
                dj = -1
            elif dj == -1:
                di = -1
                dj = 0
            else:
                di = 1
                dj = 0
    return True

with open("input.txt") as f:
    grid = [[c for c in l] for l in f.read().split("\n")]

si, sj = find_guard_location(grid)

num_candidates = 0
for oi in range(len(grid)):
    for oj in range(len(grid[oi])):
        new_grid = [[c for c in l] for l in grid]
        new_grid[oi][oj] = "#"
        if is_loop(new_grid, si, sj):
            num_candidates += 1

print(num_candidates)
