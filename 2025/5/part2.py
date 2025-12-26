def parse_input():
    with open("input.txt") as f:
        lines = f.read().splitlines()
    fresh = []
    for l in lines:
        if l.find("-") != -1:
            fresh.append([int(x) for x in l.split("-")])

    return sorted(fresh, key=lambda x: x[0])

def make_non_overlapping(fresh_intervals):
    better = [fresh_intervals[0]]
    for i  in range(1, len(fresh_intervals)):
        if fresh_intervals[i][0] <= better[-1][1]:
            better[-1][1] = max(better[-1][1], fresh_intervals[i][1])
        else:
            better.append(fresh_intervals[i])
    return better

def solution():
    fresh = parse_input()
    fresh = make_non_overlapping(fresh)
    num_fresh = 0
    for interval in fresh:
        num_fresh += interval[1] - interval[0] + 1
    print(num_fresh)

if __name__ == "__main__":
    solution()
