file = open("input.txt", "r")
lines = list(map(lambda x: x.rstrip("\n"), file.readlines()))
file.close()
lines = list(map(lambda x: x[10:], lines))

def extract_nums(nums):
    return list(map(lambda x: int(x), filter(lambda x: x.isdigit(), map(lambda x: x.strip(), nums))))

total_points = 0
for card in lines:
    nums = card.split("|")
    winning_nums = set(extract_nums(nums[0].split(" ")))
    my_nums = extract_nums(nums[1].split(" "))
    matches = 0
    for num in my_nums:
        if num in winning_nums:
            matches += 1
    if matches > 0:
        total_points += 2 ** (matches-1)

print(total_points)
