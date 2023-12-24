file = open("input.txt", "r")
lines = file.readlines()
file.close()

max_allowed_color_quantities = {
    "red": 12,
    "green": 13,
    "blue": 14,
}

def parse_game_id(game: str) -> int:
    game = game.removeprefix("Game ")
    if game[1] == ":":
        return int(game[0])
    elif game[2] == ":":
        return int(game[:2])
    else:
        return int(game[:3])

def game_is_possible(game: str) -> bool:
    i = 4
    while game[i] != ":":
        i += 1
    i += 2 # skip colon and space
    game = game[i:len(game)-1]
    reveals = game.split("; ")
    for reveal in reveals:
        colors_and_quantites = reveal.split(", ")
        for color_and_quant in colors_and_quantites:
            a = color_and_quant.split(" ")
            quantity = int(a[0])
            color = a[1]
            if quantity > max_allowed_color_quantities[color]:
                return False
    return True

possible_game_id_sum = 0
for game in lines:
    if game_is_possible(game):
        possible_game_id_sum += parse_game_id(game)

print(possible_game_id_sum)
