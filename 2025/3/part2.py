def parse_input():
    with open("input.txt") as f:
        return [[int(x) for x in bank] for bank in f.read().splitlines()]
    
def get_max_joltage(bank):
    batteries = [0] * 12
    for i in range(len(bank)):
        for j in range(len(batteries) - min(len(batteries), len(bank) - i), len(batteries)):
            if bank[i] > batteries[j]:
                batteries[j] = bank[i]
                for k in range(j+1, len(batteries)):
                    batteries[k] = 0
                break
    return int("".join(str(x) for x in batteries))

def solution():
    banks = parse_input()
    total_joltage = 0
    for bank in banks:
        total_joltage += get_max_joltage(bank)
    print(total_joltage)

if __name__ == "__main__":
    solution()
