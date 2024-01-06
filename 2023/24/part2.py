import numpy as np

file = open("input.txt", "r")
lines = list(map(lambda x: x.rstrip("\n"), file.readlines()))
file.close()

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

hails = [line_to_hail(line) for line in lines]

# we have the following equations to solve:
# P + ti * V = Pi + ti * Vi
# where the ti's, Pi's, and Vi's are the time of collision, start point, and velocity of each hailstone
# and P and V are the start point and velocity of the rock
#
# This gives us three equations, isolating for ti in each gives:
# x + ti * vx = Pi + ti * vxi
# x - Pi = ti * (vxi - vx)
# ti = (x - xi) / (vxi - vx), ti = (y - yi) / (vyi - vy), ...
#
# Then, setting (1) and (2) equal, we get:
# (x - xi) / (vxi - vx) = (y - yi) / (vyi - vy)
# (x - xi) * (vyi - vy) = (y - yi) * (vxi - vx)
# x * vyi - x * vy - xi * vyi + xi * vy = y * vxi - y * vx - yi * vxi + yi * vx
# - x * vy + y * vx = y * vxi - yi * vxi + yi * vx - x * vyi + xi * vyi - xi * vy
#
# This holds for arbitrary i and the lhs never changes, so we can set the rhs equal to itself with i replaced by j for some j != i
# y * vxi - yi * vxi + yi * vx - x * vyi + xi * vyi - xi * vy = y * vxj - yj * vxj + yj * vx - x * vyj + xj * vyj - xj * vy
# - yi * vxi + xi * vyi + yj * vxj - xj * vyj = (vyj - vyi) * x + (vxi - vxj) * y + (yi - yj) * vx + (xj - xi) * vy
# we get similar equations by using x,z and y,z instead of x,y. This gives 3 equations in 6 unknowns. We use another k != j, i to get the other 3.

# hailstones used
i = hails[0]
j = hails[1]
k = hails[2]

A = [
    [j.vy - i.vy, i.vx - j.vx, 0, i.y - j.y, j.x - i.x, 0],  # using i,j and x,y
    [j.vz - i.vz, 0, i.vx - j.vx, i.z - j.z, 0, j.x - i.x],  # using i,j and x,z
    [0, j.vz - i.vz, i.vy - j.vy, 0, i.z - j.z, j.y - i.y],  # using i,j and y,z
    [k.vy - i.vy, i.vx - k.vx, 0, i.y - k.y, k.x - i.x, 0],  # using k,j and x,y
    [k.vz - i.vz, 0, i.vx - k.vx, i.z - k.z, 0, k.x - i.x],  # using k,j and x,z
    [0, k.vz - i.vz, i.vy - k.vy, 0, i.z - k.z, k.y - i.y],  # using k,j and y,z
]
b = [
    i.x * i.vy + j.y * j.vx - i.y * i.vx - j.x * j.vy,  # using i,j and x,y
    i.x * i.vz + j.z * j.vx - i.z * i.vx - j.x * j.vz,  # using i,j and x,z
    i.y * i.vz + j.z * j.vy - i.z * i.vy - j.y * j.vz,  # using i,j and y,z
    i.x * i.vy + k.y * k.vx - i.y * i.vx - k.x * k.vy,  # using i,k and x,y
    i.x * i.vz + k.z * k.vx - i.z * i.vx - k.x * k.vz,  # using i,k and x,z
    i.y * i.vz + k.z * k.vy - i.z * i.vy - k.y * k.vz,  # using i,k and y,z
]
x = np.linalg.solve(A, b)
x0, y0, z0 = -x[0], -x[1], -x[2]
print(x0 + y0 + z0)
