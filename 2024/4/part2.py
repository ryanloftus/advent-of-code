with open("input.txt") as f:
    wordsearch = f.read().split("\n")

def is_x_mas(i, j, g):
    return ((g[i+1][j+1] == "S" and g[i-1][j-1] == "M") or (g[i+1][j+1] == "M" and g[i-1][j-1] == "S")) \
       and ((g[i+1][j-1] == "S" and g[i-1][j+1] == "M") or (g[i+1][j-1] == "M" and g[i-1][j+1] == "S"))

count = 0
for i in range(1, len(wordsearch)-1):
    for j in range(1, len(wordsearch[i])-1):
        if wordsearch[i][j] == "A" and is_x_mas(i, j, wordsearch):
            count += 1

print(count)
