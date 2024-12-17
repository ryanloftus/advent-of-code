from collections import defaultdict

def is_correct(update, rules):
    # if update = [u1, u2, ...] is incorrect, there exists ui, uj, in the update with i<j such that there is a rule uj|ui
    seen = set()
    for page_num in update:
        if len(seen.intersection(rules[page_num])) > 0:
            return False
        seen.add(page_num)
    return True

with open("input.txt") as f:
    input = [l.strip() for l in f.readlines()]

break_idx = input.index("")
updates = [l.split(",") for l in input[break_idx+1:]]

rules = defaultdict(set) # page # -> set of page #s that must come before
for rule in input[:break_idx]:
    rule_parts = rule.split("|")
    rules[rule_parts[0]].add(rule_parts[1])

middle_num_sum = 0

for update in updates:
    if is_correct(update, rules):
        middle_num_sum += int(update[len(update)//2])

print(middle_num_sum)
