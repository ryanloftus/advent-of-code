def segment_size(disk, start):
    k = disk[start]
    size = 0
    for i in range(start, len(disk)):
        if disk[i] != k:
            break
        size += 1
    return size

with open("input.txt") as f:
    disk_map = [int(x) for x in f.read()]

disk = []
segments = []
for i in range(len(disk_map)):
    if i % 2 == 0:
        segments.append((i//2, len(disk), disk_map[i]))
        disk += [i//2 for _ in range(disk_map[i])]
    else:
        disk += ["." for _ in range(disk_map[i])]

while segments:
    id, start, size = segments.pop()
    for i in range(start):
        if disk[i] != ".":
            continue
        if segment_size(disk, i) >= size:
            for j in range(size):
                disk[i+j] = disk[start+j]
                disk[start+j] = "."
            break

checksum = 0
for i in range(len(disk)):
    if disk[i] != ".":
        checksum += i * disk[i]
print(checksum)
