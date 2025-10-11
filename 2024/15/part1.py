DIRECTION = {
    "^": (0,-1),
    "v": (0,1),
    ">": (1,0),
    "<": (-1,0)
}

def parse_file():
    warehouse = []
    moves = []

    with open("input.txt") as f:
        lines = f.read().splitlines()
        i = 0
        while lines[i].startswith("#"):
            warehouse.append([c for c in lines[i]])
            i += 1
        while i < len(lines):
            for c in lines[i]:
                moves.append(c)
            i += 1
    
    return (warehouse, moves)

def get_robot_position(warehouse):
    for y in range(len(warehouse)):
        for x in range(len(warehouse[y])):
            if warehouse[y][x] == "@":
                return (x, y)
    raise Exception("robot not found")

def next_free_position(rx, ry, dx, dy, warehouse):
    while warehouse[ry+dy][rx+dx] == "O":
        rx += dx
        ry += dy
    if warehouse[ry+dy][rx+dx] == ".":
        return (rx+dx, ry+dy)
    return None

def perform_move(warehouse, move, rx, ry):
    dx, dy = DIRECTION[move]

    free_position = next_free_position(rx, ry, dx, dy, warehouse)
    if free_position is None:
        return (rx, ry)
    
    freex, freey = free_position

    warehouse[ry][rx] = "."

    rx += dx
    ry += dy
    warehouse[ry][rx] = "@"

    if freex != rx or freey != ry:
        warehouse[freey][freex] = "O"

    return (rx, ry)

def calculate_score(warehouse):
    gps_sum = 0
    for y in range(len(warehouse)):
        for x in range(len(warehouse[y])):
            if warehouse[y][x] == "O":
                gps_sum += 100 * y + x
    return gps_sum

warehouse, moves = parse_file()

rx, ry = get_robot_position(warehouse)

for move in moves:
    rx, ry = perform_move(warehouse, move, rx, ry)

with open("output.txt", 'w') as f:
    f.write("\n".join(["".join(l) for l in warehouse]))

gps_sum = calculate_score(warehouse)
print(gps_sum)
