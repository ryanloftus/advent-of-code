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
        if n in g:
            for neighbour in g[n]:
                paths += dfs(neighbour)
        memo[n] = paths
        return paths

    return dfs(s)


def solution():
    g = parse_input()
    svr_dac_fft_out = count_st_paths(g, "svr", "dac") * count_st_paths(g, "dac", "fft") * count_st_paths(g, "fft", "out")
    svr_fft_dac_out = count_st_paths(g, "svr", "fft") * count_st_paths(g, "fft", "dac") * count_st_paths(g, "dac", "out")
    print(svr_dac_fft_out + svr_fft_dac_out)

if __name__ == "__main__":
    solution()