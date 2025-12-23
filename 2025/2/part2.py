def parse_input():
    with open("input.txt") as f:
        ranges = [r.split("-") for r in f.read().split(",")]
        return [(int(r[0]), int(r[1])) for r in ranges]
    
def get_max_digits(ranges):
    largest = max(x[1] for x in ranges)
    return len(str(largest))
    
def get_all_invalid_ids(max_digits):
    invalid_ids = set()
    for digits in range(1, max_digits+1):
        for reps in range(2, digits+1):
            if digits % reps == 0:
                rep_len = digits // reps
                for n in range(10**(rep_len-1), 10**rep_len):
                    invalid_ids.add(str(n) * reps)
    return [int(id) for id in invalid_ids]

def is_id_in_a_range(id, ranges):
    for r in ranges:
        s, e = r
        if s <= id and id <= e:
            return True

    return False

def solution():
    ranges = parse_input()
    answer = 0
    max_digits = get_max_digits(ranges)
    invalid_id_candidates = get_all_invalid_ids(max_digits)
    for id in invalid_id_candidates:
        if is_id_in_a_range(id, ranges):
            answer += id
            
    print(answer)

if __name__ == "__main__":
    solution()