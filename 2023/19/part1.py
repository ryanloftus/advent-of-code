file = open("input.txt", "r")
lines = list(map(lambda x: x.rstrip("\n"), file.readlines()))
file.close()

class Part:
    def __init__(self, x, m, a, s):
        self.x = int(x)
        self.m = int(m)
        self.a = int(a)
        self.s = int(s)

    def rating(self):
        return self.x + self.m + self.a + self.s
    
    def get_attr_by_str(self, s):
        if s == "x":
            return self.x
        if s == "m":
            return self.m
        if s == "a":
            return self.a
        if s == "s":
            return self.s

workflows = dict()
i = 0
while len(lines[i]) != 0:
    partitioned_line = lines[i].partition("{")
    workflow_name = partitioned_line[0]
    rules = partitioned_line[2].strip("}").split(",")
    workflows[workflow_name] = rules
    i += 1

parts = []
i += 1
while i < len(lines):
    part_def = list(map(lambda x: int(x[2:]), lines[i].strip("{}").split(",")))
    part = Part(part_def[0], part_def[1], part_def[2], part_def[3])
    parts.append(part)
    i += 1

def try_match_rule(part, rule):
    attr = rule[0]
    part_attr = part.get_attr_by_str(attr)
    comp = rule[1]
    rule_partition = rule.partition(":")
    val = int(rule_partition[0][2:])
    next_state = rule_partition[2]
    return next_state if (comp == ">" and part_attr > val) or (comp == "<" and part_attr < val) else None

def should_accept(part):
    state = "in"
    while state != "R" and state != "A":
        rules = workflows[state]
        state = None
        for i in range(len(rules) - 1):
            state = try_match_rule(part, rules[i])
            if state != None:
                break
        if state == None:
            state = rules[-1]
    return state == "A"

accepted_parts = []
for part in parts:
    if should_accept(part):
        accepted_parts.append(part)

rating_sum = 0
for part in accepted_parts:
    rating_sum += part.rating()
print(rating_sum)
