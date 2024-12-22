from collections import defaultdict

DIRECTIONS = [(1,0), (0,1), (-1,0), (0,-1)]

def is_point_in_grid(grid, i, j):
    return i >= 0 and j >= 0 and i < len(grid) and j < len(grid[i])

def dfs(grid, i, j, seen):
    plant = grid[i][j]
    s = [(i, j)]
    area = 0
    perimeter = 0
    fences = defaultdict(list) # direction(vertical or horizontal), index on inside of fence, index_outside of fence => index of fence
    while s:
        i, j = s.pop()
        if (i,j) in seen:
            continue
        seen.add((i,j))
        area += 1
        for di, dj in DIRECTIONS:
            if is_point_in_grid(grid, i+di, j+dj) and grid[i+di][j+dj] == plant:
                s.append((i+di, j+dj))
            elif di != 0:
                fences[("horizontal", i, i+di)].append(j)
            else:
                fences[("vertical", j, j+dj)].append(i)
    for k, v in fences.items():
        perimeter += 1
        fence_indices = sorted(v)
        for i in range(1, len(fence_indices)):
            if fence_indices[i] - fence_indices[i-1] > 1:
                perimeter += 1
    return area, perimeter

with open("input.txt") as f:
    garden = [[c for c in line] for line in f.read().split("\n")]

price = 0
seen = set()
for i in range(len(garden)):
    for j in range(len(garden[i])):
        a, p = dfs(garden, i, j, seen)
        price += a * p
print(price)
