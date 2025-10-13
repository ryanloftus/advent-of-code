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
            return True
        blocked.add((i, j))
        heappush(q, (i-1, j, pathlen+1))
        heappush(q, (i+1, j, pathlen+1))
        heappush(q, (i, j-1, pathlen+1))
        heappush(q, (i, j+1, pathlen+1))
    return False

def bin_search(mem_size, falling_bytes):
    l = 1024
    r = len(falling_bytes)
    while l < r:
        m = l + (r-l)//2
        fallen_bytes = set(falling_bytes[:m])
        is_path_safe = bfs(mem_size, fallen_bytes)
        if is_path_safe:
            l = m+1
        else:
            r = m
    if not bfs(mem_size, set(falling_bytes[:l])):
        l -= 1
    return falling_bytes[l], l

def solution():
    mem_size = 71
    falling_bytes = parse_input()
    blocking_byte, idx = bin_search(mem_size, falling_bytes)
    print(",".join(str(x) for x in blocking_byte))

if __name__ == "__main__":
    solution()
