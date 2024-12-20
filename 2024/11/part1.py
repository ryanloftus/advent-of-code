with open("input.txt") as f:
    stones = [int(x) for x in f.read().split(" ")]

def get_stones_after_blink(stones):
    new_stones = []
    for stone in stones:
        stonestr = str(stone)
        if stone == 0:
            new_stones.append(1)
        elif len(stonestr) % 2 == 0:
            new_stones.append(int(stonestr[:len(stonestr)//2]))
            new_stones.append(int(stonestr[len(stonestr)//2:]))
        else:
            new_stones.append(stone * 2024)
    return new_stones

blinks = 25
for i in range(blinks):
    stones = get_stones_after_blink(stones)
print(len(stones))