file = open("input.txt", "r")
lines = list(map(lambda x: x.rstrip("\n"), file.readlines()))
file.close()
lines = list(map(lambda x: x[10:], lines))


def extract_nums(nums):
    return list(map(lambda x: int(x), filter(lambda x: x.isdigit(), map(lambda x: x.strip(), nums))))

copies = dict()
for i in range(len(lines)):
    copies[i] = 1
for i in range(len(lines)):
    card = lines[i]
    nums = card.split("|")
    winning_nums = set(extract_nums(nums[0].split(" ")))
    my_nums = extract_nums(nums[1].split(" "))
    matches = 0
    for num in my_nums:
        if num in winning_nums:
            matches += 1
    for j in range(1, matches+1):
        copies[i+j] += copies[i]

num_cards = 0
for card, num_copies in copies.items():
    num_cards += num_copies

print(num_cards)
