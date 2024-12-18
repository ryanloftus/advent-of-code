from collections import defaultdict

def is_point_in_grid(grid, i, j):
    if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[i]):
        return False
    return True

with open("input.txt") as f:
    grid = [[c for c in l] for l in f.read().split("\n")]

antennas = defaultdict(list)
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] != ".":
            antennas[grid[i][j]].append((i,j))

antinodes = set()
for freq, locations in antennas.items():
    for k in range(len(locations)):
        for l in range(k+1, len(locations)):
            i1, j1 = locations[k]
            i2, j2 = locations[l]
            di = i2 - i1
            dj = j2 - j1
            if is_point_in_grid(grid, i1-di, j1-dj):
                antinodes.add((i1-di, j1-dj))
            if is_point_in_grid(grid, i2+di, j2+dj):
                antinodes.add((i2+di, j2+dj))

print(len(antinodes))
