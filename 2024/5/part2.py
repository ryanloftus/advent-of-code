from collections import defaultdict
from random import shuffle

def get_all_nodes(g):
    nodes = set()
    for k, v in g.items():
        nodes.add(k)
        nodes = nodes.union(v)
    return nodes

def topsort(g):
    finish_order = []
    visited = set()

    def dfs(n):
        nonlocal visited
        nonlocal finish_order
        nonlocal g

        if n in visited:
            return
        visited.add(n)
        for neighbour in g[n]:
            dfs(neighbour)
        finish_order.append(n)

    for node in get_all_nodes(g):
        dfs(node)
    reversed_finish_order = finish_order[::-1]

    order_map = defaultdict(lambda: -1)
    for i in range(len(reversed_finish_order)):
        order_map[reversed_finish_order[i]] = i
    return order_map

def fix_update(update, rules):
    g = defaultdict(set)
    for k, v in rules.items():
        if k in update:
            g[k] = set(filter(lambda x: x in update, v))
    order_map = topsort(g)
    fixed_update = sorted((order_map[v], v) for v in update)
    fixed_update = [e[1] for e in fixed_update]
    if not is_correct(fixed_update, g):
        print("bad", update, "=>", fixed_update)
        exit(1)
    return fixed_update

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
updates = [[int(x) for x in l.split(",")] for l in input[break_idx+1:]]

rules = defaultdict(set) # page # -> list of page #s that must come before
for rule in input[:break_idx]:
    rule_parts = [int(x) for x in rule.split("|")]
    rules[rule_parts[0]].add(rule_parts[1])

middle_num_sum = 0

for update in updates:
    if not is_correct(update, rules):
        fixed_update = fix_update(update, rules)
        middle_num_sum += fixed_update[len(fixed_update)//2]

print(middle_num_sum)
