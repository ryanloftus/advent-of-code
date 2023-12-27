file = open("input.txt", "r")
lines = list(map(lambda x: x.rstrip("\n"), file.readlines()))
file.close()

si = 0
sj = 0
for i in range(len(lines)):
    for j in range(len(lines[i])):
        if lines[i][j] == "S":
            si = i
            sj = j

def get_next_node_from(pi, pj, ci, cj):
    curpipe = lines[ci][cj]
    if curpipe == "|":
        if pi < ci:
            return (ci+1, cj)
        else:
            return (ci-1, cj)
    if curpipe == "-":
        if pj < cj:
            return (ci, cj+1)
        else:
            return (ci, cj-1)
    if curpipe == "7":
        if pi == ci:
            return (ci+1, cj)
        else:
            return (ci, cj-1)
    if curpipe == "F":
        if pi == ci:
            return (ci+1, cj)
        else:
            return (ci, cj+1)
    if curpipe == "J":
        if pi == ci:
            return (ci-1, cj)
        else:
            return (ci, cj-1)
    if curpipe == "L":
        if pi == ci:
            return (ci-1, cj)
        else:
            return (ci, cj+1)

# obtain path that forms the cycle
path = [(si, sj)]
i = si + 1
j = sj
while not (i == si and j == sj):
    if i == 0 and j == 0:
        print("bad")
    path.append((i, j))
    i, j = get_next_node_from(path[-2][0], path[-2][1], i, j)
path.append((si, sj))

# use Shoelace Formula to get area of polygon formed by cycle
def determinant(a, b, c, d):
    return a*d - b*c

determinant_sum = 0
for i in range(len(path) - 1):
    determinant_sum += determinant(path[i][0], path[i+1][0], path[i][1], path[i+1][1])
area = determinant_sum // 2

# use Pick's Theorem to get number of internal points
internal_points = area + 1 - (len(path) -1) // 2
print(internal_points)
