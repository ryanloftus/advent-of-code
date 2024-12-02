with open("input.txt") as f:
    lines = f.readlines()

def get_diffs(a):
    return [a[i] - a[i-1] for i in range(1, len(a))]

def are_diffs_safe(diffs):
    return all(diff >= 1 and diff <= 3 for diff in diffs) or all(diff <= -1 and diff >= -3 for diff in diffs)

safe_reports = 0
for line in lines:
    nums = [int(x) for x in line.strip().split(" ")]
    diffs = get_diffs(nums)
    is_safe = are_diffs_safe(diffs)
    if not is_safe:
        for i in range(len(nums)):
            new_nums = nums[:i] + nums[i+1:]
            new_diffs = get_diffs(new_nums)
            if are_diffs_safe(new_diffs):
                is_safe = True
                break
    if is_safe:
        safe_reports += 1

print(safe_reports)
