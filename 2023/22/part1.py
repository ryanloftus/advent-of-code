file = open("input.txt", "r")
lines = list(map(lambda x: x.rstrip("\n"), file.readlines()))
file.close()

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

blocks = [line_to_block(line) for line in lines]
blocks.sort(key=lambda b: b.min_z())

supports = [list() for _ in range(len(blocks))]
supported_by = [list() for _ in range(len(blocks))]
for i in range(len(blocks)):
    while min(blocks[i].p1.z, blocks[i].p2.z) > 1:
        resting = False
        for j in range(i):
            if falls_on(blocks[i], blocks[j]):
                resting = True
                supports[j].append(i)
                supported_by[i].append(j)
        if resting:
            break
        blocks[i].p1.z -= 1
        blocks[i].p2.z -= 1

num_disintegratable = 0
for i in range(len(blocks)):
    is_disintegratable = True
    for j in supports[i]:
        if len(supported_by[j]) == 1:
            is_disintegratable = False
            break
    if is_disintegratable:
        num_disintegratable += 1
print(num_disintegratable)
