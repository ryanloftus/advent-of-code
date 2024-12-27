from collections import defaultdict

class Robot:
    def __init__(self, s, height, width):
        s = s.split(" ")
        pos = s[0].split("=")[1].split(",")
        v = s[1].split("=")[1].split(",")
        self.px = int(pos[0])
        self.py = int(pos[1])
        self.vx = int(v[0])
        self.vy = int(v[1])
        self.area_height = height
        self.area_width = width

    def move(self):
        self.px = (self.px + self.vx) % self.area_width
        self.py = (self.py + self.vy) % self.area_height

def write_to_file(robots):
    robots = sorted(robots, key=lambda x: (x.py, x.px))
    ri = 0
    with open("output.txt", "w") as f:
        for y in range(robots[0].area_height):
            for x in range(robots[0].area_width):
                n = 0
                while ri < len(robots) and robots[ri].px == x and robots[ri].py == y:
                    ri += 1
                    n += 1
                f.write(" " if n == 0 else "X")
            f.write("\n")

def longest_sequence(nums):
    longest = 0
    current = 1
    for i in range(1, len(nums)):
        if nums[i] == nums[i-1] + 1:
            current += 1
            longest = max(longest, current)
        else:
            current = 0
    return longest

def is_christmas_tree(robots):
    """
    idea: Christams tree image will have a straight horizontal line
    above the trunk
    """
    line_candidates = defaultdict(set)
    for robot in robots:
        line_candidates[robot.py].add(robot.px)
    for k, v in line_candidates.items():
        l = sorted(v)
        if longest_sequence(l) >= 10:
            return True
    return False

width = 101
height = 103

with open("input.txt") as f:
    robots = [Robot(line, height, width) for line in f.read().split("\n")]

for seconds in range(1, 10002):
    for robot in robots:
        robot.move()
    if is_christmas_tree(robots):
        write_to_file(robots)
        print(seconds)
        exit(0)
