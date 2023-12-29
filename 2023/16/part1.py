from queue import Queue

file = open("input.txt", "r")
lines = list(map(lambda x: x.rstrip("\n"), file.readlines()))
file.close()

def translate(i, j, dir):
    if dir == "r":
        return (i, j + 1)
    elif dir == "l":
        return (i, j - 1)
    elif dir == "u":
        return (i - 1, j)
    else:
        return (i + 1, j)

def add_if_valid_and_new(i, j, dir, q, energized):
    if i < 0 or i >= len(lines) or j < 0 or j >= len(lines[i]):
        return
    if (i,j) in energized and dir in energized[(i,j)]:
        return
    q.put((i, j, dir))
    if (i,j) in energized:
        energized[(i,j)].append(dir)
    else:
        energized[(i,j)] = [dir]

energized = dict()
energized[(0,0)] = ["r"]
q = Queue()
q.put((0, 0, "r"))

while not q.empty():
    i, j, dir = q.get()
    if lines[i][j] == ".":
        next_i, next_j = translate(i, j, dir)
        add_if_valid_and_new(next_i, next_j, dir, q, energized)
    elif lines[i][j] == "-":
        if dir == "r" or dir == "l":
            next_i, next_j = translate(i, j, dir)
            add_if_valid_and_new(next_i, next_j, dir, q, energized)
        else:
            li, lj = translate(i, j, "l")
            add_if_valid_and_new(li, lj, "l", q, energized)
            ri, rj = translate(i, j, "r")
            add_if_valid_and_new(ri, rj, "r", q, energized)
    elif lines[i][j] == "|":
        if dir == "u" or dir == "d":
            next_i, next_j = translate(i, j, dir)
            add_if_valid_and_new(next_i, next_j, dir, q, energized)
        else:
            ui, uj = translate(i, j, "u")
            add_if_valid_and_new(ui, uj, "u", q, energized)
            di, dj = translate(i, j, "d")
            add_if_valid_and_new(di, dj, "d", q, energized)
    elif lines[i][j] == "\\":
        new_dir = None
        if dir == "r":
            new_dir = "d"
        elif dir == "l":
            new_dir = "u"
        elif dir == "u":
            new_dir = "l"
        else:
            new_dir = "r"
        next_i, next_j = translate(i, j, new_dir)
        add_if_valid_and_new(next_i, next_j, new_dir, q, energized)
    elif lines[i][j] == "/":
        new_dir = None
        if dir == "r":
            new_dir = "u"
        elif dir == "l":
            new_dir = "d"
        elif dir == "u":
            new_dir = "r"
        else:
            new_dir = "l"
        next_i, next_j = translate(i, j, new_dir)
        add_if_valid_and_new(next_i, next_j, new_dir, q, energized)
    else:
        print("unexpected symbol: " + lines[i][j])
        exit(1)

print(len(energized))
