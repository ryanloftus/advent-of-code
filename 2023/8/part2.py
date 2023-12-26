from math import lcm

file = open("input.txt", "r")
lines = list(map(lambda x: x.rstrip("\n"), file.readlines()))
file.close()

seq = lines[0]
nodes = dict()
starting_nodes = []
for i in range(2, len(lines)):
    node = lines[i].split(" = ")
    nodename = node[0]
    nodepaths = node[1].strip("()").split(", ")
    nodes[nodename] = { "L": nodepaths[0], "R": nodepaths[1] }
    if nodename.endswith("A"):
        starting_nodes.append(nodename)

def reached_dest(locs):
    for loc in locs:
        if not loc.endswith("Z"):
            return False
    return True

step = 0
cycles = []
for i in range(len(starting_nodes)):
    n = starting_nodes[i]
    step = 0
    cycles.append([])
    while len(cycles[-1]) < 4:
        n = nodes[n][seq[step % len(seq)]]
        step += 1
        if n.endswith("Z"):
            cycles[-1].append(step)

print(starting_nodes)
print(cycles)
# observe that cycles follow a pattern, if it takes n steps to get to end the first time, it takes n steps to get back to end each other time

cycle_lengths = list(map(lambda x: x[0], cycles))
print(cycle_lengths)  # prints: [22357, 17263, 14999, 16697, 13301, 20659]

print(lcm(22357, 17263, 14999, 16697, 13301, 20659))
