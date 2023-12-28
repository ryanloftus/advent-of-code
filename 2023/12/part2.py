file = open("input.txt", "r")
lines = list(map(lambda x: x.rstrip("\n"), file.readlines()))
file.close()

def unfold(line):
    spattern = line[0]
    npattern = line[1]
    for _ in range(4):
        spattern += "?"
        spattern += line[0]
        npattern += ","
        npattern += line[1]
    npattern = list(map(lambda x: int(x), npattern.split(",")))
    return (spattern, npattern)

def num_blocks(spattern, block_size):
    blocks = get_blocks(spattern, block_size, is_last_block=True)
    return len(blocks)

def get_blocks(spattern, block_size, is_last_block=False):
    blocks = []
    current_contiguous = 0
    for i in range(0, len(spattern)):
        if spattern[i] == ".":
            current_contiguous = 0
        else:
            current_contiguous += 1
            if current_contiguous >= block_size:
                blocks.append(i - block_size + 1)
    i = 0
    while i < len(blocks):
        if ("#" in spattern[:blocks[i]]) or (blocks[i] > 0 and spattern[blocks[i] - 1] == "#") or (blocks[i] + block_size < len(spattern) and spattern[blocks[i] + block_size] == "#"):
            blocks.remove(blocks[i])
        elif is_last_block and blocks[i] + block_size < len(spattern) and "#" in spattern[blocks[i] + block_size:]:
            blocks.remove(blocks[i])
        else:
            i += 1
    return blocks

def num_arrangements(spattern, npattern):
    dp = [[0] * len(npattern) for _ in range(len(spattern))]
    for i in range(len(dp) - 1, -1, -1):
        spattern_suffix = spattern[i:]
        dp[i][-1] = num_blocks(spattern_suffix, npattern[-1])
        for j in range(len(dp[i]) - 2, -1, -1):
            block_size = npattern[j]
            blocks = get_blocks(spattern_suffix, block_size)
            for block in blocks:
                if i + block + block_size + 1 < len(dp):
                    dp[i][j] += dp[i + block + block_size + 1][j + 1]
    return dp[0][0]

arrangements_sum = 0
for i in range(len(lines)):
    record = lines[i].split(" ")
    spattern, npattern = unfold(record)
    arrangements_sum += num_arrangements(spattern, npattern)
    if i % 50 == 49:
        print("finished " + str(i+1))
print(arrangements_sum)
