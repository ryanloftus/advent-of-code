file = open("input.txt", "r")
lines = list(map(lambda x: x.rstrip("\n"), file.readlines()))
file.close()

patterns = []
patterns.append([])
for line in lines:
    if len(line) == 0:
        patterns.append([])
    else:
        patterns[-1].append(line)


def get_refl_value(pattern):
    # check for reflection across vertical line
    for j in range(1, len(pattern[0])):
        num_smudges = 0
        for i in range(len(pattern)):
            h = min(len(pattern[0]) - 1, 2 * j - 1)
            l = max(0, j - (h - j) - 1)
            while l < h:
                if pattern[i][l] != pattern[i][h]:
                    num_smudges += 1
                l += 1
                h -= 1
        if num_smudges == 1:
            return j

    # check for reflection across horizontal line
    for i in range(1, len(pattern)):
        num_smudges = 0
        h = min(len(pattern) - 1, 2 * i - 1)
        l = max(0, i - (h - i) - 1)
        while l < h:
            for j in range(len(pattern[0])):
                if pattern[l][j] != pattern[h][j]:
                    num_smudges += 1
            l += 1
            h -= 1
        if num_smudges == 1:
            return i * 100

    print("no refl")
    for l in pattern:
        print(l)
    exit(1)


pattern_sum = 0
for pattern in patterns:
    pattern_sum += get_refl_value(pattern)
print(pattern_sum)
