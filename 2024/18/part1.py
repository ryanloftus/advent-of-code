from heapq import *

def parse_input():
    with open("input.txt") as f:
        return [tuple(int(x) for x in line.split(",")) for line in f.read().splitlines()]
    
def bfs(mem_size, blocked):
    q = [(0, 0, 0)]
    while q:
        i, j, pathlen = heappop(q)
        if (i, j) in blocked or i < 0 or i >= mem_size or j < 0 or j >= mem_size:
            continue
        if i == mem_size - 1 and j == mem_size - 1:
            return pathlen
        blocked.add((i, j))
        heappush(q, (i-1, j, pathlen+1))
        heappush(q, (i+1, j, pathlen+1))
        heappush(q, (i, j-1, pathlen+1))
        heappush(q, (i, j+1, pathlen+1))
    return None

def solution():
    num_fallen = 1024
    mem_size = 71
    falling_bytes = parse_input()
    fallen_bytes = set(falling_bytes[:num_fallen])
    min_dist = bfs(mem_size, fallen_bytes)
    print(min_dist)

if __name__ == "__main__":
    solution()
