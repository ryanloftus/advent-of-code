from collections import defaultdict

def parse_input():
    with open("input.txt") as f:
        return f.read().splitlines()
    
def find_start(grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "S":
                return i, j

def get_or_zero(m, i, j):
    if i < 0 or j < 0 or i >= len(m) or j >= len(m[i]):
        return 0
    return m[i][j]

def count_timelines(grid, si, sj):
    dp = [[1 for _ in range(len(grid[i]))] for i in range(len(grid))]
    for i in range(len(grid)-2, -1, -1):
        for j in range(len(grid[i])):
            if grid[i][j] == "^":
                dp[i][j] = get_or_zero(dp, i+1, j-1) + get_or_zero(dp, i+1, j+1)
            else:
                dp[i][j] = get_or_zero(dp, i+1, j)
    return dp[si][sj]

def solution():
    grid = parse_input()
    si, sj = find_start(grid)
    timelines = count_timelines(grid, si, sj)
    print(timelines)

if __name__ == "__main__":
    solution()
