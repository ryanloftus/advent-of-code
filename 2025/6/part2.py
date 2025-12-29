class Problem:
    def __init__(self, operator, nums):
        self.op = operator
        self.nums = nums

    def solve(self):
        if self.op == "*":
            product = 1
            for n in self.nums:
                product *= n
            return product
        else:
            return sum(self.nums)
    
    def debug(self):
        print(self.op.join(f" {n} " for n in self.nums))

def col_to_num(grid: list[list[str]], col):
    num = None
    for i in range(len(grid)):
        if not grid[i][col].isnumeric():
            continue
        if num is None:
            num = 0
        num *= 10
        num += int(grid[i][col])
    return num

def parse_input():
    with open("input.txt") as f:
        lines = f.read().splitlines()
    problems = []
    curnums = []
    curop = None
    for i in range(len(lines[0])):
        if lines[-1][i] != " ":
            if curop is not None:
                problems.append(Problem(curop, curnums))
            curop = lines[-1][i]
            curnums = []
        curnum = col_to_num(lines, i)
        if curnum is not None:
            curnums.append(curnum)
    problems.append(Problem(curop, curnums))
    return problems

def solution():
    problems = parse_input()
    grand_total = sum(p.solve() for p in problems)
    print(grand_total)

if __name__ == "__main__":
    solution()
