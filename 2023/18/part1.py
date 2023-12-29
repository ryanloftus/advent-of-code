file = open("input.txt", "r")
lines = list(map(lambda x: x.rstrip("\n"), file.readlines()))
file.close()

def translate(i, j, dir, dist):
    if dir == "R":
        return (i, j + dist)
    if dir == "L":
        return (i, j - dist)
    if dir == "U":
        return (i - dist, j)
    if dir == "D":
        return (i + dist, j)

path = [(0, 0)]
path_volume = 0
for line in lines:
    split_line = line.split(" ")
    dir = split_line[0]
    dist = int(split_line[1])
    next_point = translate(path[-1][0], path[-1][1], dir, dist)
    path.append(next_point)
    path_volume += dist

# use Shoelace Formula to get area of polygon formed by cycle
def determinant(a, b, c, d):
    return a*d - b*c

determinant_sum = 0
for i in range(len(path) - 1):
    determinant_sum += determinant(path[i][0], path[i+1][0], path[i][1], path[i+1][1])
area = abs(determinant_sum // 2)

# use Pick's Theorem to get number of internal points
internal_points = area + 1 - path_volume // 2 # path_volume = external_points
interior_volume = internal_points
total_lava_volume = path_volume + interior_volume
print(total_lava_volume)
