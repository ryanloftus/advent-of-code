file = open("input.txt", "r")
lines = list(map(lambda x: x.rstrip("\n"), file.readlines()))
file.close()

seq = lines[0]
nodes = dict()
for i in range(2, len(lines)):
    node = lines[i].split(" = ")
    nodename = node[0]
    nodepaths = node[1].strip("()").split(", ")
    nodes[nodename] = { "L": nodepaths[0], "R": nodepaths[1] }

step = 0
node = "AAA"
while node != "ZZZ":
    node = nodes[node][seq[step % len(seq)]]
    step += 1
print(step)
