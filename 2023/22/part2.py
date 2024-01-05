import os.path

class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

class Block:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def max_x(self):
        return max(self.p1.x, self.p2.x)

    def max_y(self):
        return max(self.p1.y, self.p2.y)

    def max_z(self):
        return max(self.p1.z, self.p2.z)

    def min_x(self):
        return min(self.p1.x, self.p2.x)

    def min_y(self):
        return min(self.p1.y, self.p2.y)

    def min_z(self):
        return min(self.p1.z, self.p2.z)

def falls_on(b1, b2):
    "returns true if b1 is directly on top of b2"
    if b1.min_z() - 1 != b2.max_z():
        return False
    if b1.p1.x == b1.p2.x and b1.p1.y == b1.p2.y:
        return b1.p1.x >= b2.min_x() and b1.p1.x <= b2.max_x() and \
            b1.p1.y >= b2.min_y() and b1.p1.y <= b2.max_y()
    if b2.p1.x == b2.p2.x and b2.p1.y == b2.p2.y:
        return b2.p1.x >= b1.min_x() and b2.p1.x <= b1.max_x() and \
            b2.p1.y >= b1.min_y() and b2.p1.y <= b1.max_y()
    if b1.p2.x == b1.p1.x and b2.p2.x == b2.p1.x:
        return b1.p1.x == b2.p1.x and ((b1.max_y() >= b2.min_y() and b1.max_y() <= b2.max_y()) or
                                       (b1.min_y() >= b2.min_y() and b1.min_y() <= b2.max_y()) or
                                       (b2.max_y() >= b1.min_y() and b2.max_y() <= b1.max_y()) or
                                       (b2.min_y() >= b1.min_y() and b2.min_y() <= b1.max_y()))
    if b1.p2.y == b1.p1.y and b2.p2.y == b2.p1.y:
        return b1.p1.y == b2.p1.y and ((b1.max_x() >= b2.min_x() and b1.max_x() <= b2.max_x()) or
                                       (b1.min_x() >= b2.min_x() and b1.min_x() <= b2.max_x()) or
                                       (b2.max_x() >= b1.min_x() and b2.max_x() <= b1.max_x()) or
                                       (b2.min_x() >= b1.min_x() and b2.min_x() <= b1.max_x()))
    if b1.p1.x == b1.p2.x:
        return b1.p1.x >= b2.min_x() and b1.p1.x <= b2.max_x() and \
            b2.p1.y >= b1.min_y() and b2.p1.y <= b1.max_y()
    return b1.p1.y >= b2.min_y() and b1.p1.y <= b2.max_y() and \
        b2.p1.x >= b1.min_x() and b2.p1.x <= b1.max_x()

def str_to_point(s: str):
    parr = [int(c) for c in s.split(",")]
    return Point(parr[0], parr[1], parr[2])

def line_to_block(line: str):
    p = line.partition("~")
    p1 = str_to_point(p[0])
    p2 = str_to_point(p[2])
    return Block(p1, p2)

def settle_blocks(blocks):
    blocks.sort(key=lambda b: b.min_z())
    for i in range(len(blocks)):
        while min(blocks[i].p1.z, blocks[i].p2.z) > 1:
            resting = False
            for j in range(i):
                if falls_on(blocks[i], blocks[j]):
                    resting = True
                    break
            if resting:
                break
            blocks[i].p1.z -= 1
            blocks[i].p2.z -= 1

def create_settled_state_file(blocks):
    settle_blocks(blocks)
    f = open("settled_state.txt", "w")
    for b in blocks:
        f.write("{},{},{}~{},{},{}\n".format(b.p1.x, b.p1.y, b.p1.z, b.p2.x, b.p2.y, b.p2.z))
    f.close()

if not os.path.isfile("settled_state.txt"):
    f = open("input.txt", "r")
    lines = list(map(lambda x: x.rstrip("\n"), f.readlines()))
    f.close()
    blocks = [line_to_block(line) for line in lines]
    create_settled_state_file(blocks)

f = open("settled_state.txt")
lines = list(map(lambda x: x.rstrip("\n"), f.readlines()))
f.close()
blocks = [line_to_block(line) for line in lines]

supports = [set() for _ in range(len(blocks))]
supported_by = [set() for _ in range(len(blocks))]
for i in range(len(blocks)):
    for j in range(i):
        if falls_on(blocks[i], blocks[j]):
            supports[j].add(i)
            supported_by[i].add(j)

deps = [set() for _ in range(len(blocks))] # if deps[i] contains j, then if i disintegrates, j will fall
for i in range(len(blocks)):
    for j in supports[i]:
        if len(supported_by[j]) == 1:
            deps[i].add(j)

def add_transitive_deps(i):
    for j in range(i+1, len(blocks)):
        if len(supported_by[j]) == 0: continue
        is_dep = True
        for s in supported_by[j]:
            if s not in deps[i]:
                is_dep = False
                break
        if is_dep: deps[i].add(j)

for i in range(len(blocks)):
    add_transitive_deps(i)
total_deps = sum(map(lambda x: len(x), deps))
print(total_deps)
