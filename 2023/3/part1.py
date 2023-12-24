file = open("input.txt", "r")
lines = list(map(lambda x: x.rstrip("\n"), file.readlines()))
file.close()
w = len(lines[0])

def contains_symbol(s: str):
    for c in s:
        if not c.isdigit() and c != ".":
            return True
    return False

def is_part_num(i, num_start, num_end):
    surrounding_info = ""
    if num_start > 0:
        surrounding_info += lines[i][num_start-1]
    if num_end + 1 < w:
        surrounding_info += lines[i][num_end+1]
    if i > 0:
        surrounding_info += lines[i-1][max(0, num_start-1):min(w, num_end+2)]
    if i + 1 < len(lines):
        surrounding_info += lines[i+1][max(0, num_start-1):min(w, num_end+2)]
    return contains_symbol(surrounding_info)

part_number_sum = 0
for i in range(len(lines)):
    num_start = -1
    for j in range(w):
        if num_start != -1 and (not lines[i][j].isdigit() or j == w - 1):
            num_end = j if lines[i][j].isdigit() else j-1
            if is_part_num(i, num_start, num_end):
                part_number_sum += int(lines[i][num_start:num_end+1])
            num_start = -1
        elif num_start == -1 and lines[i][j].isdigit():
            num_start = j
            if j == w-1 and is_part_num(i, num_start, j):
                part_number_sum += int(lines[i][j])
                num_start = -1

print(part_number_sum)
