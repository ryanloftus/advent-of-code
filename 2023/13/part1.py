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
        is_reflection = True
        for i in range(len(pattern)):
            h = min(len(pattern[0]) - 1, 2 * j - 1)
            l = max(0, j - (h - j) - 1)
            while l < h:
                if pattern[i][l] != pattern[i][h]:
                    is_reflection = False
                    break
                l += 1
                h -= 1
            if not is_reflection:
                break
        if is_reflection:
            return j

    # check for reflection across horizontal line
    for i in range(1, len(pattern)):
        is_reflection = True
        h = min(len(pattern) - 1, 2 * i - 1)
        l = max(0, i - (h - i) - 1)
        while l < h:
            if pattern[l] != pattern[h]:
                is_reflection = False
                break
            l += 1
            h -= 1
        if is_reflection:
            return i * 100
        
    print("no refl")
    for l in pattern:
        print(l)
    exit(1)

pattern_sum = 0
for pattern in patterns:
    pattern_sum += get_refl_value(pattern)
print(pattern_sum)
