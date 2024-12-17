def find_guard_location(grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "^":
                return i, j
    raise "security guard not found!"

with open("input.txt") as f:
    grid = f.read().split("\n")

i, j = find_guard_location(grid)
di = -1
dj = 0

visited = set()

while True:
    visited.add((i, j))
    if i+di < 0 or i+di >= len(grid) or j+dj < 0 or j+dj >= len(grid[i]):
        break
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

print(len(visited))
