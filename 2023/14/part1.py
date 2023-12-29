file = open("input.txt", "r")
platform = list(map(lambda x: x.rstrip("\n"), file.readlines()))
file.close()

h = len(platform)
w = len(platform[0])

def calc_load():
    load_per_rock = 0
    total_load = 0
    for i in range(h - 1, -1, -1):
        load_per_rock += 1
        for j in range(w):
            if platform[i][j] == "O":
                total_load += load_per_rock
    return total_load

def move_rock_up(i, j):
    while i > 0 and platform[i-1][j] == ".":
        platform[i-1] = platform[i-1][:j] + "O" + platform[i-1][j+1:]
        platform[i] = platform[i][:j] + "." + platform[i][j+1:]
        i -= 1

for i in range(h):
    for j in range(w):
        if platform[i][j] == "O":
            move_rock_up(i, j)

load = calc_load()
print(load)
