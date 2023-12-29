file = open("input.txt", "r")
platform = list(map(lambda x: [c for c in x.rstrip("\n")], file.readlines()))
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

def move_rock_north(i, j):
    while i > 0 and platform[i-1][j] == ".":
        platform[i-1][j] = "O"
        platform[i][j] = "."
        i -= 1

def move_rock_south(i, j):
    while i + 1 < h and platform[i+1][j] == ".":
        platform[i+1][j] = "O"
        platform[i][j] = "."
        i += 1

def move_rock_east(i, j):
    while j + 1 < w and platform[i][j+1] == ".":
        platform[i][j+1] = "O"
        platform[i][j] = "."
        j += 1

def move_rock_west(i, j):
    while j > 0 and platform[i][j-1] == ".":
        platform[i][j-1] = "O"
        platform[i][j] = "."
        j -= 1

def tilt_north():
    for i in range(h):
        for j in range(w):
            if platform[i][j] == "O":
                move_rock_north(i, j)

def tilt_south():
    for i in range(h-1, -1, -1):
        for j in range(w):
            if platform[i][j] == "O":
                move_rock_south(i, j)

def tilt_east():
    for i in range(h):
        for j in range(w-1, -1, -1):
            if platform[i][j] == "O":
                move_rock_east(i, j)

def tilt_west():
    for i in range(h):
        for j in range(w):
            if platform[i][j] == "O":
                move_rock_west(i, j)

def hash_cur_state():
    state_hash = []
    for i in range(h):
        for j in range(w):
            if platform[i][j] == "O":
                state_hash.append(i * 10000 + j)
    return tuple(state_hash)

# idea: there is probably a *relatively* short cycle that we are repeating
states = dict()
i = 0
while i < 1000000000:
    tilt_north()
    tilt_west()
    tilt_south()
    tilt_east()
    state_hash = hash_cur_state()
    if state_hash in states:
        cycle_len = i - states[state_hash]
        while i < 1000000000 - cycle_len:
            i += cycle_len
    states[state_hash] = i
    i += 1

load = calc_load()
print(load)
