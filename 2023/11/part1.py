file = open("input.txt", "r")
lines = list(map(lambda x: x.rstrip("\n"), file.readlines()))
file.close()

def col_is_empty(col):
    for i in range(len(lines)):
        if lines[i][col] == "#":
            return False
    return True

def insert_blank_col_after(col):
    for i in range(len(lines)):
        lines[i] = lines[i][:col+1] + "." + lines[i][col+1:]

i = 0
while i < len(lines):
    if "#" not in lines[i]:
        lines.insert(i, lines[i])
        i += 2
    else:
        i += 1

i = 0
while i < len(lines[0]):
    if col_is_empty(i):
        insert_blank_col_after(i)
        i += 2
    else:
        i += 1

galaxies = []
for i in range(len(lines)):
    for j in range(len(lines[0])):
        if lines[i][j] == "#":
            galaxies.append((i,j))

shortest_paths_sum = 0
for i in range(len(galaxies)):
    for j in range(i+1, len(galaxies)):
        shortest_paths_sum += abs(galaxies[i][0] - galaxies[j][0]) + abs(galaxies[i][1] - galaxies[j][1])
print(shortest_paths_sum)
