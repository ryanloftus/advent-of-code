def parse_input():
    with open("input.txt") as f:
        ranges = [r.split("-") for r in f.read().split(",")]
        return ranges

def invalid_ids_in_range(r):
    s = int(r[0])
    e = int(r[1])
    invalid = []
    while s <= e:
        ss = str(s)
        if len(ss) % 2 == 1:
            s = int("1" + "0" * len(ss))
            continue
        halflen = len(ss)//2
        lhs = int(ss[:halflen])
        rhs = int(ss[halflen:])
        if lhs > rhs:
            s = lhs * (10 ** halflen) + lhs
        elif lhs == rhs:
            invalid.append(s)
            s += 1
        else:
            s += 1

    if len(invalid) == 0:
        print(f"no invalid ids in {r}")
    else:
        print(f"found invalid ids {invalid} in {r}")
    

    return invalid

def solution():
    ranges = parse_input()
    answer = 0
    for r in ranges:
        answer += sum(invalid_ids_in_range(r))
    print(answer)

if __name__ == "__main__":
    solution()