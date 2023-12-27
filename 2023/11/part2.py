file = open("input.txt", "r")
lines = list(map(lambda x: x.rstrip("\n"), file.readlines()))
file.close()


def col_is_empty(col):
    for i in range(len(lines)):
        if lines[i][col] == "#":
            return False
    return True

def get_shortest_path(i1, j1, i2, j2):
    min_i = min(i1, i2)
    max_i = max(i1, i2)
    min_j = min(j1, j2)
    max_j = max(j1, j2)
    dist = 0
    for i in range(min_i + 1, max_i + 1):
        dist += 1000000 if i in expanded_rows else 1
    for j in range(min_j + 1, max_j + 1):
        dist += 1000000 if j in expanded_cols else 1
    return dist

expanded_rows = set()
for i in range(len(lines)):
    if "#" not in lines[i]:
        expanded_rows.add(i)

expanded_cols = set()
for i in range(len(lines[0])):
    if col_is_empty(i):
        expanded_cols.add(i)

galaxies = []
for i in range(len(lines)):
    for j in range(len(lines[0])):
        if lines[i][j] == "#":
            galaxies.append((i, j))

shortest_paths_sum = 0
for i in range(len(galaxies)):
    for j in range(i+1, len(galaxies)):
        shortest_paths_sum += get_shortest_path(galaxies[i][0], galaxies[i][1], galaxies[j][0], galaxies[j][1])
print(shortest_paths_sum)
