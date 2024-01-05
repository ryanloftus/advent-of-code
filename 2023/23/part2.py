from queue import Queue

file = open("input.txt", "r")
lines = list(map(lambda x: [c for c in x.rstrip("\n")], file.readlines()))
file.close()

si = 0
sj = 1
ti = len(lines) - 1
tj = len(lines[0]) - 2


def try_add_bfs(q, newi, newj, d, visited):
    if lines[newi][newj] != "#" and (newi, newj) not in visited:
        visited.add((newi, newj))
        q.put_nowait((newi, newj, d + 1))

def add_adj_bfs(q, i, j, d, visited):
    if i > 0:
        try_add_bfs(q, i-1, j, d, visited)
    if i + 1 < len(lines):
        try_add_bfs(q, i+1, j, d, visited)
    if j > 0:
        try_add_bfs(q, i, j-1, d, visited)
    if j + 1 < len(lines[0]):
        try_add_bfs(q, i, j+1, d, visited)

# too slow: create a graph where nodes are the points where multiple directions are available (i.e. more than 2 of surrounding 4 are non-# tiles)
# run bfs from each node to find which other nodes are reachable
# find the longest path in the new graph

g = dict()
g[(si, sj)] = []
g[(ti, tj)] = []
for i in range(len(lines)):
    for j in range(len(lines[0])):
        if lines[i][j] == "#": continue
        available_dirs = 0
        if i > 0 and lines[i-1][j] != "#":
            available_dirs += 1
        if i + 1 < len(lines) and lines[i+1][j] != "#":
            available_dirs += 1
        if j > 0 and lines[i][j-1] != "#":
            available_dirs += 1
        if j + 1 < len(lines[0])  and lines[i][j+1] != "#":
            available_dirs += 1
        if available_dirs > 2:
            g[(i, j)] = []

def bfs(starti, startj):
    visited = set()
    visited.add((starti, startj))
    q = Queue()
    q.put_nowait((starti, startj, 0))
    edges = []
    while not q.empty():
        i, j, dist = q.get_nowait()
        if (i, j) in g and (i != starti or j != startj):
            edges.append((i, j, dist))
        else:
            add_adj_bfs(q, i, j, dist, visited)
    return edges

for k in g.keys():
    g[k] = bfs(k[0], k[1])

def try_add_dfs(stack, newi, newj, d, path):
    if (newi, newj) not in path:
        newpath = path.copy()
        newpath.add((newi, newj))
        stack.append((newi, newj, d, newpath))

def add_adj_dfs(stack, i, j, d, path):
    for ni, nj, nd in g[(i, j)]:
        try_add_dfs(stack, ni, nj, d + nd, path)

def dfs():
    longest_simple_path = 0
    stack = []
    spath = set()
    spath.add((0, 1))
    stack.append((0, 1, 0, spath))
    while len(stack) > 0:
        i, j, dist, path = stack.pop()
        if i == ti and j == tj:
            longest_simple_path = max(longest_simple_path, dist)
            continue
        add_adj_dfs(stack, i, j, dist, path)
    return longest_simple_path

longest_simple_path = dfs()
print(longest_simple_path)
