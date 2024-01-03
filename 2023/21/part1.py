from queue import Queue

file = open("input.txt", "r")
lines = list(map(lambda x: [c for c in x.rstrip("\n")], file.readlines()))
file.close()
N = len(lines)

def find_start():
    for i in range(N):
        for j in range(N):
            if lines[i][j] == "S":
                return i, j


si, sj = find_start()
lines[si][sj] = "."


visited_even = set()
visited_odd = set()
q = Queue()

TOTAL_STEPS = 64


def add(i, j, steps):
    if lines[i][j] != "." or (i, j) in visited_even or (i, j) in visited_odd:
        return
    if steps % 2 == 0:
        visited_even.add((i, j))
    else:
        visited_odd.add((i, j))
    if steps != TOTAL_STEPS:
        q.put_nowait((i, j, steps))


def add_adj(i, j, steps):
    steps += 1
    if i > 0:
        add(i-1, j, steps)
    if i + 1 < N:
        add(i+1, j, steps)
    if j > 0:
        add(i, j-1, steps)
    if j + 1 < N:
        add(i, j+1, steps)


add(si, sj, 0)
last_s = 0
while not q.empty():
    i, j, steps = q.get_nowait()
    add_adj(i, j, steps)

if TOTAL_STEPS % 2 == 0:
    print(len(visited_even))
else:
    print(len(visited_odd))
