from heapq import *

DIR_EAST = (1,0)
DIR_WEST = (-1,0)
DIR_NORTH = (0,-1)
DIR_SOUTH = (0,1)

DIRS = [DIR_EAST, DIR_WEST, DIR_NORTH, DIR_SOUTH]

def parse_input():
    with open("input.txt") as f:
        return [[c for c in line] for line in f.read().splitlines()]

def find_start(maze):
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if maze[i][j] == "S":
                return (i,j)
    raise Exception("Start not found")

def count_good_tiles(maze):
    q = []
    si,sj = find_start(maze)
    visited = dict()
    heappush(q, (0, si, sj, DIR_EAST, []))

    good_tiles = set()

    target_score = 10**10

    while q:
        score, i, j, dir, path = heappop(q)

        if score > target_score:
            break

        if ((i, j, dir) in visited and score > visited[(i, j, dir)]) or maze[i][j] == "#":
            continue

        if maze[i][j] == "E":
            target_score = min(target_score, score)
            for tile in path:
                good_tiles.add(tile)
                good_tiles.add((i, j))
            continue
        
        visited[(i, j, dir)] = score

        for d in DIRS:
            heappush(q, (score+1000, i, j, d, path))
        
        heappush(q, (score+1, i+dir[0], j+dir[1], dir, path+[(i,j)]))

    return len(good_tiles)

def solution():
    maze = parse_input()
    num_good_tiles = count_good_tiles(maze)
    print(num_good_tiles)

if __name__ == "__main__":
    solution()
