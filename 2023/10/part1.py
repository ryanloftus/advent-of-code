from queue import Queue

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

# From looking at input, two ends of S in cycle are below and to the left. We can bfs from each of these nodes and see where they meet.
seen_one = dict()
seen_two = dict()
bfs_one = Queue()
bfs_two = Queue()
bfs_one.put((si+1, sj, 1))
bfs_two.put((si, sj-1, 1))
seen_one[(si, sj)] = 0
seen_two[(si, sj)] = 0
seen_one[(si+1, sj)] = 1
seen_two[(si, sj-1)] = 1

def connects_below(pipe):
    return pipe == "F" or pipe == "|" or pipe == "7"

def connects_above(pipe):
    return pipe == "L" or pipe == "|" or pipe == "J"

def connects_left(pipe):
    return pipe == "7" or pipe == "J" or pipe == "-"

def connects_right(pipe):
    return pipe == "L" or pipe == "F" or pipe == "-"

def try_add_above(q, i, j, d, g, seen):
    if i > 0 and ((i-1, j) not in seen) and connects_below(g[i-1][j]):
        q.put((i-1, j, d+1))
        seen[(i-1, j)] = d+1

def try_add_below(q, i, j, d, g, seen):
    if i < len(g) - 1 and ((i+1, j) not in seen) and connects_above(g[i+1][j]):
        q.put((i+1, j, d+1))
        seen[(i+1, j)] = d+1

def try_add_left(q, i, j, d, g, seen):
    if j > 0 and ((i, j-1) not in seen) and connects_right(g[i][j-1]):
        q.put((i, j-1, d+1))
        seen[(i, j-1)] = d+1

def try_add_right(q, i, j, d, g, seen):
    if j < len(g[0]) - 1 and ((i, j+1) not in seen) and connects_left(g[i][j+1]):
        q.put((i, j+1, d+1))
        seen[(i, j+1)] = d+1

def add_adj(q, i, j, d, g, seen):
    if g[i][j] == "|":
        try_add_above(q, i, j, d, g, seen)
        try_add_below(q, i, j, d, g, seen)
    elif g[i][j] == "-":
        try_add_left(q, i, j, d, g, seen)
        try_add_right(q, i, j, d, g, seen)
    elif g[i][j] == "7":
        try_add_left(q, i, j, d, g, seen)
        try_add_below(q, i, j, d, g, seen)
    elif g[i][j] == "L":
        try_add_right(q, i, j, d, g, seen)
        try_add_above(q, i, j, d, g, seen)
    elif g[i][j] == "J":
        try_add_left(q, i, j, d, g, seen)
        try_add_above(q, i, j, d, g, seen)
    elif g[i][j] == "F":
        try_add_right(q, i, j, d, g, seen)
        try_add_below(q, i, j, d, g, seen)

while not bfs_one.empty() and not bfs_two.empty():
    i1, j1, dist1 = bfs_one.get()
    i2, j2, dist2 = bfs_two.get()
    if (i1, j1) in seen_two:
        print(min(dist1, seen_two[(i1, j1)]))
        break
    if (i2, j2) in seen_one:
        print(min(dist2, seen_one[(i2, j2)]))
        break
    add_adj(bfs_one, i1, j1, dist1, lines, seen_one)
    add_adj(bfs_two, i2, j2, dist2, lines, seen_two)
