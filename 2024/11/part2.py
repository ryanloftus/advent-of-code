with open("input.txt") as f:
    stones = [int(x) for x in f.read().split(" ")]

def get_num_stones_after_blinks(stone, blinks, memo):
    if blinks == 0:
        return 1
    elif (stone, blinks) in memo:
        return memo[(stone, blinks)]
    num_stones = 0
    stonestr = str(stone)
    if stone == 0:
        num_stones += get_num_stones_after_blinks(1, blinks-1, memo)
    elif len(stonestr) % 2 == 0:
        num_stones += get_num_stones_after_blinks(int(stonestr[:len(stonestr)//2]), blinks-1, memo)
        num_stones += get_num_stones_after_blinks(int(stonestr[len(stonestr)//2:]), blinks-1, memo)
    else:
        num_stones += get_num_stones_after_blinks(stone * 2024, blinks-1, memo)
    memo[(stone, blinks)] = num_stones
    return num_stones

memo = dict()
blinks = 75

num_stones = 0
for stone in stones:
    num_stones += get_num_stones_after_blinks(stone, blinks, memo)
print(num_stones)