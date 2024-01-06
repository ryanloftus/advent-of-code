import numpy as np

file = open("input.txt", "r")
lines = list(map(lambda x: x.rstrip("\n"), file.readlines()))
file.close()

MIN_BOX = 200000000000000
MAX_BOX = 400000000000000

class Hail:
    def __init__(self, x, y, z, vx, vy, vz):
        self.x = x
        self.y = y
        self.z = z
        self.vx = vx
        self.vy = vy
        self.vz = vz

def line_to_hail(line: str):
    part = line.partition(" @ ")
    p = [int(x) for x in part[0].split(", ")]
    v = [int(v) for v in part[2].split(", ")]
    return Hail(p[0], p[1], p[2], v[0], v[1], v[2])

def collide_in_test_area(h1: Hail, h2: Hail):
    m1 = h1.vy / h1.vx
    m2 = h2.vy / h2.vx
    b1 = h1.y - (m1 * h1.x)
    b2 = h2.y - (m2 * h2.x)
    a = [[-m1, 1], [-m2, 1]]
    b = [b1, b2]
    try:
        poi = np.linalg.solve(a, b)
        if poi[0] > MAX_BOX or poi[0] < MIN_BOX or poi[1] > MAX_BOX or poi[1] < MIN_BOX:
            return False
        if (poi[0] > h1.x and h1.vx < 0) or (poi[0] > h2.x and h2.vx < 0) or (poi[0] < h1.x and h1.vx > 0) or (poi[0] < h2.x and h2.vx > 0):
            return False
        return True
    except:
        return False

hails = [line_to_hail(line) for line in lines]

test_area_collisions = 0
for i in range(len(hails)):
    for j in range(i + 1, len(hails)):
        if collide_in_test_area(hails[i], hails[j]):
            test_area_collisions += 1
print(test_area_collisions)
