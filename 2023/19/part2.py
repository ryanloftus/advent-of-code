from queue import Queue

file = open("input.txt", "r")
lines = list(map(lambda x: x.rstrip("\n"), file.readlines()))
file.close()

class PartRange:
    def __init__(self, xrange, mrange, arange, srange):
        self.xrange = xrange
        self.mrange = mrange
        self.arange = arange
        self.srange = srange

    def range_size(self, r):
        return r[1] - r[0] + 1

    def size(self):
        return self.range_size(self.xrange) * self.range_size(self.mrange) * self.range_size(self.arange) * self.range_size(self.srange)
    
    def get_attr_by_str(self, attr_str):
        if attr_str == "x":
            return self.xrange
        if attr_str == "m":
            return self.mrange
        if attr_str == "a":
            return self.arange
        if attr_str == "s":
            return self.srange
        
    def update_range(self, attr, new_pr_attr_range, cur_pr_attr_range):
        new_pr = PartRange(self.xrange, self.mrange, self.arange, self.srange)
        if attr == "x":
            new_pr.xrange = new_pr_attr_range
            self.xrange = cur_pr_attr_range
        elif attr == "m":
            new_pr.mrange = new_pr_attr_range
            self.mrange = cur_pr_attr_range
        elif attr == "a":
            new_pr.arange = new_pr_attr_range
            self.arange = cur_pr_attr_range
        elif attr == "s":
            new_pr.srange = new_pr_attr_range
            self.srange = cur_pr_attr_range
        return new_pr

    def apply_rule(self, rule):
        attr = rule[0]
        comp = rule[1]
        part_attr_min, part_attr_max = self.get_attr_by_str(attr)
        rule_partition = rule.partition(":")
        val = int(rule_partition[0][2:])
        next_state = rule_partition[2]
        if comp == "<":
            if part_attr_max < val:
                new_part_range = PartRange(self.xrange, self.mrange, self.arange, self.srange)
                self.xrange = (0, -1)
                return new_part_range, next_state
            elif part_attr_min >= val:
                return empty_range(), next_state
            else:
                new_part_range = self.update_range(attr, (part_attr_min, val-1), (val, part_attr_max))
                return new_part_range, next_state
        else:
            if part_attr_min > val:
                new_part_range = PartRange(self.xrange, self.mrange, self.arange, self.srange)
                self.xrange = (0, -1)
                return new_part_range, next_state
            elif part_attr_max <= val:
                return empty_range(), next_state
            else:
                new_part_range = self.update_range(attr, (val+1, part_attr_max), (part_attr_min, val))
                return new_part_range, next_state

def empty_range():
    return PartRange((0,-1),(0,-1),(0,-1),(0,-1))

workflows = dict()
i = 0
while len(lines[i]) != 0:
    partitioned_line = lines[i].partition("{")
    workflow_name = partitioned_line[0]
    rules = partitioned_line[2].strip("}").split(",")
    workflows[workflow_name] = rules
    i += 1

part_ranges = Queue()
part_ranges.put((PartRange((1,4000), (1,4000), (1,4000), (1,4000)), "in"))
accepted_part_ranges = []
while not part_ranges.empty():
    pr, state = part_ranges.get()
    rules = workflows[state]
    for i in range(len(rules) - 1):
        new_pr, new_state = pr.apply_rule(rules[i])
        if new_pr.size() > 0:
            if new_state == "A":
                accepted_part_ranges.append(new_pr)
            elif new_state != "R":
                part_ranges.put((new_pr, new_state))
        if pr.size() <= 0:
            break
    if pr.size() > 0:
        if rules[-1] == "A":
            accepted_part_ranges.append(pr)
        elif rules[-1] != "R":
            part_ranges.put((pr, rules[-1]))

num_accepted_combinations = sum(map(lambda x: x.size(), accepted_part_ranges))
print(num_accepted_combinations)
