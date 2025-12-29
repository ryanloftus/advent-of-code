def parse_line(line):
    return [int(x) for x in line.split(" ") if x != ""]

def parse_input():
    with open("input.txt") as f:
        lines = f.read().splitlines()
    nums = [parse_line(line) for line in lines[:len(lines)-1]]
    operators = [x for x in lines[-1].split(" ") if x != ""]
    return nums, operators

def add_col(nums, col):
    return sum(nums[row][col] for row in range(len(nums)))

def multiply_col(nums, col):
    product = 1
    for row in range(len(nums)):
        product *= nums[row][col]
    return product

def solution():
    nums, operators = parse_input()
    solutions = []
    for i in range(len(operators)):
        sol = add_col(nums, i) if operators[i] == "+" else multiply_col(nums, i)
        solutions.append(sol)
    print(sum(solutions))

if __name__ == "__main__":
    solution()
