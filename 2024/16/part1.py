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

def bfs(maze):
    q = []
    si,sj = find_start(maze)
    visited = set()
    heappush(q, (0, si, sj, DIR_EAST))

    while q:
        score, i, j, dir = heappop(q)

        if (i, j, dir) in visited or maze[i][j] == "#":
            continue

        if maze[i][j] == "E":
            return score
        
        visited.add((i, j, dir))

        for d in DIRS:
            heappush(q, (score+1000, i, j, d))
        
        heappush(q, (score+1, i+dir[0], j+dir[1], dir))
        
    raise Exception("End not found")


def solution():
    maze = parse_input()
    lowest_score = bfs(maze)
    print(lowest_score)

if __name__ == "__main__":
    solution()
