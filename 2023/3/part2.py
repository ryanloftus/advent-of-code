file = open("input.txt", "r")
lines = list(map(lambda x: x.rstrip("\n"), file.readlines()))
file.close()
w = len(lines[0])

gears = dict()
for i in range(len(lines)):
    for j in range(w):
        if lines[i][j] == "*":
            gears[(i,j)] = []

def check_adj_gears(i, num_start, num_end):
    partnum = int(lines[i][num_start:num_end+1])
    for gear in gears.keys():
        if gear[0] >= i-1 and gear[0] <= i+1 and gear[1] >= num_start-1 and gear[1] <= num_end+1:
            gears[gear].append(partnum)
    return

for i in range(len(lines)):
    num_start = -1
    for j in range(w):
        if num_start != -1 and (not lines[i][j].isdigit() or j == w - 1):
            num_end = j if lines[i][j].isdigit() else j-1
            check_adj_gears(i, num_start, num_end)
            num_start = -1
        elif num_start == -1 and lines[i][j].isdigit():
            num_start = j
            if j == w-1:
                check_adj_gears(i, j, j)
                num_start = -1

gear_ratio_sum = 0
for gear, adj in gears.items():
    if len(adj) == 2:
        gear_ratio_sum += adj[0] * adj[1]

print(gear_ratio_sum)
