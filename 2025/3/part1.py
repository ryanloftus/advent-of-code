def parse_input():
    with open("input.txt") as f:
        return [[int(x) for x in bank] for bank in f.read().splitlines()]
    
def get_max_joltage(bank):
    d1 = 0
    d2 = 0
    for i in range(len(bank)):
        if bank[i] > d1 and i < len(bank)-1:
            d1 = bank[i]
            d2 = 0
        elif bank[i] > d2:
            d2 = bank[i]
    return d1 * 10 + d2

def solution():
    banks = parse_input()
    total_joltage = 0
    for bank in banks:
        total_joltage += get_max_joltage(bank)
    print(total_joltage)

if __name__ == "__main__":
    solution()
