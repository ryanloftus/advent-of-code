import matplotlib.pyplot as plt

def parse_input():
    with open("input.txt") as f:
        return [[int(x) for x in line.split(",")] for line in f.read().splitlines()]

def area(t1, t2):
    l = max(t1[0], t2[0]) - min(t1[0], t2[0]) + 1
    w = max(t1[1], t2[1]) - min(t1[1], t2[1]) + 1
    return l * w

def contains_only_red_and_green(t1, t2, red_tiles):
    """
    The tile rectangle is valid iff the four lines that form
    the rectangle do not cross any lines that form the polygon
    defined by red_tiles.
    This is not actually true but close enough for the particular problem.
    """
    minx = min(t1[0], t2[0])
    maxx = max(t1[0], t2[0])
    miny = min(t1[1], t2[1])
    maxy = max(t1[1], t2[1])
    for i in range(len(red_tiles)):
        dx = red_tiles[i][0] - red_tiles[i-1][0]
        if dx == 0:  # vertical line
            x = red_tiles[i][0]
            top = max(red_tiles[i][1], red_tiles[i-1][1])
            bottom = min(red_tiles[i][1], red_tiles[i-1][1])
            if minx < x and x < maxx and (
                (top >= maxy and bottom < maxy)
                or
                (top > miny and bottom <= miny)
            ):
                return False
        else:  # horizontal line
            y = red_tiles[i][1]
            right = max(red_tiles[i][0], red_tiles[i-1][0])
            left = min(red_tiles[i][0], red_tiles[i-1][0])
            if miny < y and y < maxy and (
                (right >= maxx and left < maxx)
                or
                (right > minx and left <= minx)
            ):
                return False
    return True

def solution():
    red_tiles = parse_input()
    max_area = 0
    for i in range(len(red_tiles)):
        for j in range(i+1, len(red_tiles)):
            a = area(red_tiles[i], red_tiles[j])
            if max_area < a and contains_only_red_and_green(red_tiles[i], red_tiles[j], red_tiles):
                max_area = a
    print(max_area)

def draw_polygon(red_tiles):
    x = [p[0] for p in red_tiles]
    y = [p[1] for p in red_tiles]
    plt.plot(x, y, marker='o')

    # Optional labels and title
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title("Connected Points Plot")

    plt.show()

if __name__ == "__main__":
    # draw_polygon(parse_input())
    solution()
