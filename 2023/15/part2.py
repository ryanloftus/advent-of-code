file = open("input.txt", "r")
lines = list(map(lambda x: x.rstrip("\n"), file.readlines()))
file.close()

steps = lines[0].split(",")

def holiday_ascii_string_helper(s: str):
    h = 0
    for c in s:
        h = ((h + ord(c)) * 17) % 256
    return h

boxes = [[] for _ in range(256)]
for step in steps:
    if step[-1] == "-":
        label = step[:len(step) - 1]
        box_num = holiday_ascii_string_helper(label)
        for l, fl in boxes[box_num]:
            if l == label:
                boxes[box_num].remove((l, fl))
                break
    else:
        split_step = step.partition("=")
        label = split_step[0]
        focal_length = split_step[2]
        box_num = holiday_ascii_string_helper(label)
        replaced = False
        for i in range(len(boxes[box_num])):
            l, fl = boxes[box_num][i]
            if l == label:
                boxes[box_num][i] = (l, focal_length)
                replaced = True
                break
        if not replaced:
            boxes[box_num].append((label, focal_length))

focusing_power = 0
for i in range(len(boxes)):
    for j in range(len(boxes[i])):
        focusing_power += (1 + i) * (1 + j) * int(boxes[i][j][1])
print(focusing_power)
