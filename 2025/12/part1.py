def parse_input():
    with open("input.txt", "r") as file:
        lines = file.read().splitlines()
    shapes = []
    i = 0
    while i < len(lines):
        if "x" in lines[i]:
            break
        elif ":" in lines[i]:
            shape = lines[i+1:i+4]
            shapes.append(shape)
            i += 4
        else:
            i += 1
    trees = []
    while i < len(lines):
        dims, shapes_required = lines[i].split(": ")
        dims = tuple([int(x) for x in dims.split("x")])
        shapes_required = tuple([int(x) for x in shapes_required.split(" ")])
        trees.append((dims, shapes_required))
        i += 1
    shapes = [[[1 if cell == "#" else 0 for cell in line] for line in shape] for shape in shapes]
    return shapes, trees

def is_feasible(tree, shapes_space_taken):
    dims, shapes_required = tree
    space_available = dims[0] * dims[1]
    for i, num_required in enumerate(shapes_required):
        space_available -= shapes_space_taken[i] * num_required
    return space_available >= 0

def solution():
    shapes, trees = parse_input()
    shapes_space_taken = [sum(sum(line) for line in shape) for shape in shapes]
    feasible_trees = []
    for i, tree in enumerate(trees):
        if is_feasible(tree, shapes_space_taken):
            feasible_trees.append(tree)
    print(len(feasible_trees))

if __name__ == "__main__":
    solution()