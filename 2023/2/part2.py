file = open("input.txt", "r")
lines = file.readlines()
file.close()

def parse_game_id(game: str) -> int:
    game = game.removeprefix("Game ")
    if game[1] == ":":
        return int(game[0])
    elif game[2] == ":":
        return int(game[:2])
    else:
        return int(game[:3])


def game_power(game: str) -> bool:
    i = 4
    while game[i] != ":":
        i += 1
    i += 2  # skip colon and space
    game = game[i:len(game)-1]

    min_cubes = { "red": 0, "blue": 0, "green": 0 }

    reveals = game.split("; ")
    for reveal in reveals:
        colors_and_quantites = reveal.split(", ")
        for color_and_quant in colors_and_quantites:
            a = color_and_quant.split(" ")
            quantity = int(a[0])
            color = a[1]
            min_cubes[color] = max(min_cubes[color], quantity)
    
    return min_cubes["red"] * min_cubes["blue"] * min_cubes["green"]


game_power_sum = 0
for game in lines:
    game_power_sum += game_power(game)

print(game_power_sum)
