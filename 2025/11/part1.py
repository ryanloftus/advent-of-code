def parse_input():
    g = {}
    with open("input.txt") as f:
        for l in f:
            p = l.strip("\n").partition(": ")
            g[p[0]] = p[2].split(" ")
    return g

def count_st_paths(g, s, t):
    memo = { t: 1 }

    def dfs(n):
        if n in memo:
            return memo[n]
        paths = 0
        for neighbour in g[n]:
            paths += dfs(neighbour)
        memo[n] = paths
        return paths

    return dfs(s)


def solution():
    g = parse_input()
    paths = count_st_paths(g, "you", "out")
    print(paths)

if __name__ == "__main__":
    solution()