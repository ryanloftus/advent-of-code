with open("input.txt") as f:
    lines = f.readlines()

safe_reports = 0
for line in lines:
    nums = [int(x) for x in line.strip().split(" ")]
    diffs = [nums[i] - nums[i-1] for i in range(1, len(nums))]
    if all(diff >= 1 and diff <= 3 for diff in diffs) or all(diff <= -1 and diff >= -3 for diff in diffs):
        print(diffs)
        safe_reports += 1

print(safe_reports)
