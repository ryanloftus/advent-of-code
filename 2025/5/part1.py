def parse_input():
    with open("input.txt") as f:
        lines = f.read().splitlines()
    fresh = []
    ingredients = []
    for l in lines:
        if len(l) == 0:
            continue
        elif l.find("-") == -1:
            ingredients.append(int(l))
        else:
            fresh.append([int(x) for x in l.split("-")])

    return fresh, ingredients

def is_fresh(id, fresh):
    for rng in fresh:
        if rng[0] <= id and id <= rng[1]:
            return True
    return False

def solution():
    fresh, ingredients = parse_input()
    num_fresh = 0
    for id in ingredients:
        if is_fresh(id, fresh):
            num_fresh += 1
    print(num_fresh)

if __name__ == "__main__":
    solution()
