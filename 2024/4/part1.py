with open("input.txt") as f:
    wordsearch = f.read().split("\n")

next_letter = {
    "": "X",
    "X": "M",
    "M": "A",
    "A": "S"
}

def dfs(i, j, g):
    xmas_count = 0
    s = []
    for di in range(-1,2):
        for dj in range(-1,2):
            if dj == di and dj == 0:
                continue
            s.append((i,j,"",di,dj))
    while s:
        i, j, last, di, dj = s.pop()
        if i < 0 or i >= len(g) or j < 0 or j >= len(g[i]) or g[i][j] != next_letter[last]:
            continue
        elif g[i][j] == "S":
            xmas_count += 1
            continue
        s.append((i+di,j+dj,g[i][j],di,dj))
    return xmas_count

count = 0
for i in range(len(wordsearch)):
    for j in range(len(wordsearch[i])):
        if wordsearch[i][j] == "X":
            count += dfs(i, j, wordsearch)

print(count)
