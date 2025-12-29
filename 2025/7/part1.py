from queue import Queue

def parse_input():
    with open("input.txt") as f:
        return f.read().splitlines()
    
def find_start(grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "S":
                return i, j

def count_splits(grid, si, sj):
    q = Queue()
    visited = set()
    splits = 0
    q.put_nowait((si, sj))
    while not q.empty():
        i, j = q.get_nowait()
        if (i, j) in visited:
            continue
        elif i + 1 == len(grid):
            continue
        elif grid[i+1][j] == "^":
            if j-1 >= 0:
                q.put_nowait((i+1, j-1))
            if j+1 < len(grid[i+1]):
                q.put_nowait((i+1, j+1))
            splits += 1
        else:
            q.put_nowait((i+1, j))
        visited.add((i, j))
    return splits

def solution():
    grid = parse_input()
    si, sj = find_start(grid)
    splits = count_splits(grid, si, sj)
    print(splits)

if __name__ == "__main__":
    solution()
