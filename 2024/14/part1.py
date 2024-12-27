class Robot:
    def __init__(self, s):
        s = s.split(" ")
        pos = s[0].split("=")[1].split(",")
        v = s[1].split("=")[1].split(",")
        self.px = int(pos[0])
        self.py = int(pos[1])
        self.vx = int(v[0])
        self.vy = int(v[1])

with open("input.txt") as f:
    robots = [Robot(line) for line in f.read().split("\n")]

width = 101
height = 103
seconds = 100

for robot in robots:
    robot.px = (robot.px + robot.vx * seconds) % width
    robot.py = (robot.py + robot.vy * seconds) % height

q1 = 0
q2 = 0
q3 = 0
q4 = 0
for robot in robots:
    if robot.px < width // 2:
        if robot.py < height // 2:
            q1 += 1
        elif robot.py > height // 2:
            q3 += 1
    elif robot.px > width // 2:
        if robot.py < height // 2:
            q2 += 1
        elif robot.py > height // 2:
            q4 += 1
print(q1 * q2 * q3 * q4)
