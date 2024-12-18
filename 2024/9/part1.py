from collections import deque

with open("input.txt") as f:
    disk_map = [int(x) for x in f.read()]

disk_layout = []
empty_space_q = deque()
for i in range(len(disk_map)):
    if i % 2 == 0:
        disk_layout += [i//2 for _ in range(disk_map[i])]
    else:
        for j in range(disk_map[i]):
            empty_space_q.append(len(disk_layout) + j)
        disk_layout += ["." for _ in range(disk_map[i])]

while disk_layout[-1] == ".":
    disk_layout.pop()
    empty_space_q.pop()

while len(empty_space_q) > 0:
    disk_layout[empty_space_q.popleft()] = disk_layout.pop()
    while disk_layout[-1] == ".":
        disk_layout.pop()
        empty_space_q.pop()

checksum = 0
for i in range(len(disk_layout)):
    checksum += i * disk_layout[i]
print(checksum)
