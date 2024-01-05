file = open("input.txt", "r")
lines = list(map(lambda x: [c for c in x.rstrip("\n")], file.readlines()))
file.close()

si = 0
sj = 1
ti = len(lines) - 1
tj = len(lines[0]) - 2

def try_add(stack, newi, newj, path):
    if (newi, newj) not in path:
        newpath = path.copy()
        newpath.add((newi, newj))
        if lines[newi][newj] == "v":
            newi += 1
            newpath.add((newi, newj))
        elif lines[newi][newj] == ">":
            newj += 1
            newpath.add((newi, newj))
        elif lines[newi][newj] == "<":
            newj -= 1
            newpath.add((newi, newj))
        stack.append((newi, newj, newpath))

def add_adj(stack, i, j, path):
    if i > 0 and lines[i-1][j] == ".":
        try_add(stack, i-1, j, path)
    if i + 1 < len(lines) and (lines[i+1][j] == "." or lines[i+1][j] == "v"):
        try_add(stack, i+1, j, path)
    if j > 0 and (lines[i][j-1] == "." or lines[i][j-1] == "<"):
        try_add(stack, i, j-1, path)
    if j + 1 < len(lines[0]) and (lines[i][j+1] == "." or lines[i][j+1] == ">"):
        try_add(stack, i, j+1, path)

def dfs():
    longest_simple_path = 0
    stack = []
    spath = set()
    spath.add((0, 1))
    stack.append((0, 1, spath))
    while len(stack) > 0:
        i, j, path = stack.pop()
        if i == ti and j == tj:
            longest_simple_path = max(longest_simple_path, len(path) - 1)
            continue
        add_adj(stack, i, j, path)
    return longest_simple_path

longest_simple_path = dfs()
print(longest_simple_path)
