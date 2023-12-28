file = open("input.txt", "r")
lines = list(map(lambda x: x.rstrip("\n"), file.readlines()))
file.close()

def get_combinations(spattern):
    if len(spattern) == 0:
        return [""]
    coms = get_combinations(spattern[1:])
    if spattern[0] == "?":
        new_coms = []
        for com in coms:
            new_coms.append("." + com)
            new_coms.append("#" + com)
        return new_coms
    return list(map(lambda x: spattern[0] + x, coms))

def matches_pattern(s, npattern):
    s = s.split(".")
    s = map(lambda x: x.strip("."), s)
    s = filter(lambda x: len(x) > 0, s)
    s = list(map(lambda x: len(x), s))
    if len(s) != len(npattern):
        return False
    for i in range(len(s)):
        if s[i] != npattern[i]:
            return False
    return True

def num_arrangements(spattern, npattern):
    combinations = get_combinations(spattern)
    matches = 0
    for combination in combinations:
        if matches_pattern(combination, npattern):
            matches += 1
    return matches

arrangements_sum = 0
for line in lines:
    record = line.split(" ")
    record[1] = list(map(lambda x: int(x), record[1].split(",")))
    arrangements_sum += num_arrangements(record[0], record[1])
print(arrangements_sum)
