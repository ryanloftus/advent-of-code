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

def map_num_to_dir(num):
    if num == 0:
        return "R"
    if num == 1:
        return "D"
    if num == 2:
        return "L"
    if num == 3:
        return "U"
    
def get_base_ten_number(hex_digit):
    if hex_digit.isdigit():
        return int(hex_digit)
    if hex_digit == "a":
        return 10
    if hex_digit == "b":
        return 11
    if hex_digit == "c":
        return 12
    if hex_digit == "d":
        return 13
    if hex_digit == "e":
        return 14
    if hex_digit == "f":
        return 15

def get_num_from_hex(hex_num):
    num = 0
    for d in hex_num:
        num += get_base_ten_number(d)
        num *= 16
    return num // 16

path = [(0, 0)]
path_volume = 0
for line in lines:
    hex = line.split(" ")[2].strip("()#")
    dist = get_num_from_hex(hex[0:5])
    dir = map_num_to_dir(int(hex[5]))
    next_point = translate(path[-1][0], path[-1][1], dir, dist)
    path.append(next_point)
    path_volume += dist

# use Shoelace Formula to get area of polygon formed by cycle
def determinant(a, b, c, d):
    return a*d - b*c

determinant_sum = 0
for i in range(len(path) - 1):
    determinant_sum += determinant(path[i][0],
                                   path[i+1][0], path[i][1], path[i+1][1])
area = abs(determinant_sum // 2)

# use Pick's Theorem to get number of internal points
internal_points = area + 1 - path_volume // 2  # path_volume = external_points
interior_volume = internal_points
total_lava_volume = path_volume + interior_volume
print(total_lava_volume)
