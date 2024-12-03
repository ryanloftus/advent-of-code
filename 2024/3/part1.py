import re

with open("input.txt") as f:
    program = f.read()

pattern = "(mul\([0-9]{1,3},[0-9]{1,3}\))|(do\(\))|(don't\(\))"

matches = re.findall(pattern, program)

total = 0
do = True
for mult_match, do_match, dont_match in matches:
    if do_match:
        do = True
    elif dont_match:
        do = False
    elif do:
        nums = mult_match[4:-1].split(",")
        total += int(nums[0]) * int(nums[1])

print(total)
