import re

with open("input.txt") as f:
    program = f.read()

pattern = "mul\([0-9]{1,3},[0-9]{1,3}\)"

matches = re.findall(pattern, program)

total = 0
for match in matches:
    nums = match[4:-1].split(",")
    total += int(nums[0]) * int(nums[1])

print(total)
