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

def adjust_warehouse(warehouse):
    for y in range(len(warehouse)):
        warehouse[y] = "".join(warehouse[y]).replace(".", "..").replace("O", "[]").replace("@", "@.").replace("#", "##")
        warehouse[y] = [c for c in warehouse[y]]

def get_robot_position(warehouse):
    for y in range(len(warehouse)):
        for x in range(len(warehouse[y])):
            if warehouse[y][x] == "@":
                return (x, y)
    raise Exception("robot not found")

def copy_warehouse(warehouse):
    return [
        [cell for cell in row]
        for row in warehouse
    ]

def perform_push(warehouse, rx, ry, dx, dy):
    target = warehouse[ry+dy][rx+dx]

    if target == "#":
        return False

    did_push_succeed = target == "." or (
        perform_push(warehouse, rx+dx, ry+dy, dx, dy) and \
        (
            dy == 0
            or 
            (
                (target == "]" and perform_push(warehouse, rx+dx-1, ry+dy, dx, dy))
                or
                (target == "[" and perform_push(warehouse, rx+dx+1, ry+dy, dx, dy))
            )
        )
    )

    if did_push_succeed:
        warehouse[ry+dy][rx+dx] = warehouse[ry][rx]
        warehouse[ry][rx] = "."

    return did_push_succeed

def perform_move(warehouse, move, rx, ry):
    dx, dy = DIRECTION[move]

    tmp = copy_warehouse(warehouse)

    did_push_succeed = perform_push(tmp, rx, ry, dx, dy)

    if did_push_succeed:
        return (rx+dx, ry+dy, tmp)
    
    return (rx, ry, warehouse)

def calculate_score(warehouse):
    gps_sum = 0
    for y in range(len(warehouse)):
        for x in range(len(warehouse[y])):
            if warehouse[y][x] == "[":
                gps_sum += 100 * y + x
    return gps_sum

warehouse, moves = parse_file()
adjust_warehouse(warehouse)

rx, ry = get_robot_position(warehouse)

for move in moves:
    rx, ry, warehouse = perform_move(warehouse, move, rx, ry)
    with open("output.txt", 'w') as f:
        f.write("\n".join(["".join(l) for l in warehouse]))
    if warehouse[ry][rx] != "@":
        raise Exception("bad state")


gps_sum = calculate_score(warehouse)
print(gps_sum)
