from queue import PriorityQueue

file = open("input.txt", "r")
lines = list(map(lambda x: [int(c) for c in x.rstrip("\n")], file.readlines()))
file.close()

left_of = { "r": "u", "u": "l", "l": "d", "d": "r" }
right_of = { "r": "d", "d": "l", "l": "u", "u": "r" }

def translate(i, j, dir):
    if dir == "u":
        return (i - 1, j)
    elif dir == "d":
        return (i + 1, j)
    elif dir == "r":
        return (i, j + 1)
    else:
        return (i, j - 1)

visited = set()
visited.add((0,0,"r",1))
visited.add((0,0,"d",1))
q = PriorityQueue()
q.put((0, 0, 0, "r", 1))
q.put((0, 0, 0, "d", 1))

def add_if_in_bounds(loss_so_far, ni, nj, d, same_d):
    if ni >= 0 and ni < len(lines) and nj >= 0 and nj < len(lines[0]) and (ni,nj,d,same_d) not in visited:
        q.put((loss_so_far + lines[ni][nj], ni, nj, d, same_d))
        visited.add((ni,nj,d,same_d))

while not q.empty():
    loss, i, j, dir, same_dir = q.get()
    if i == len(lines) - 1 and j == len(lines[0]) - 1:
        print(loss)
        break
    if same_dir < 3:
        next_i, next_j = translate(i, j, dir)
        add_if_in_bounds(loss, next_i, next_j, dir, same_dir + 1)
    ldir = left_of[dir]
    rdir = right_of[dir]
    li, lj = translate(i, j, ldir)
    ri, rj = translate(i, j, rdir)
    add_if_in_bounds(loss, li, lj, ldir, 1)
    add_if_in_bounds(loss, ri, rj, rdir, 1)
