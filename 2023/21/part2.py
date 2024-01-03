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

def num_reachable(num_steps):
    visited_even = set()
    visited_odd = set()
    q = Queue()

    def add(i, j, steps):
        if lines[i % N][j % N] != "." or (i, j) in visited_even or (i, j) in visited_odd:
            return
        if steps % 2 == 0:
            visited_even.add((i, j))
        else:
            visited_odd.add((i, j))
        if steps != num_steps:
            q.put_nowait((i, j, steps))

    def add_adj(i, j, steps):
        steps += 1
        add(i-1, j, steps)
        add(i+1, j, steps)
        add(i, j-1, steps)
        add(i, j+1, steps)

    add(si, sj, 0)
    while not q.empty():
        i, j, steps = q.get_nowait()
        add_adj(i, j, steps)

    return len(visited_even) if num_steps % 2 == 0 else len(visited_odd)

TOTAL_STEPS = 26501365
OFFSET = TOTAL_STEPS % N

def get_diff_arr(arr):
    diff = []
    for i in range(len(arr) - 1):
        diff.append(arr[i+1] - arr[i])
    return diff

first_five = list(map(lambda x: num_reachable(OFFSET + N * x), list(range(6))))
print(first_five)
diff_first_five = get_diff_arr(first_five)
print(diff_first_five)
second_diff_first_five = get_diff_arr(diff_first_five)
print(second_diff_first_five)

# the above code prints:
# [3885, 34700, 96215, 188430, 311345, 464960]
# [30815, 61515, 92215, 122915, 153615]
# [30700, 30700, 30700, 30700]
# ... So, the pattern is quadratic, and we want to find the value of this quadratic for x = TOTAL_STEPS // N
X = TOTAL_STEPS // N

# converting the above data into points on a cartesian plane, we can solve for a, b, and c in our quadratic f(x) = ax^2 + bx + c
# we have points: (0, 3885), (1, 34700), and (2, 96215)
# this provides the system of equations:
# 3885 = a(0)^2 + b(0) + c ->  (e1) 3885 = c
# 34700 = a(1)^2 + b(1) + c -> (e2) 30815 = a + b
# 96215 = a(2)^2 + b(2) + c -> (e3) 92330 = 4a + 2b
# we do e3 - 2*(e2) to get: 30700 = 2a -> a = 15350
# and finally: 30815 = a + b -> b = 15465
a = 15350
b = 15465
c = 3885

def quadratic(x):
    return a * x * x + b * x + c

ans = quadratic(X)
print(ans)
