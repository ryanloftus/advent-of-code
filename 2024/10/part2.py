def get_trailhead_score(map, si, sj):
    s = [(si, sj, 0)]
    score = 0
    while s:
        i, j, h = s.pop()
        if i < 0 or j < 0 or i >= len(map) or j >= len(map[i]) or h != map[i][j]:
            continue
        elif map[i][j] == 9:
            score += 1
        else:
            s.append((i+1, j, h+1))
            s.append((i-1, j, h+1))
            s.append((i, j+1, h+1))
            s.append((i, j-1, h+1))
    return score

with open("input.txt") as f:
    map = [[int(x) for x in l] for l in f.read().split("\n")]

total_score = 0
for i in range(len(map)):
    for j in range(len(map[i])):
        if map[i][j] == 0:
            total_score += get_trailhead_score(map, i, j)
print(total_score)