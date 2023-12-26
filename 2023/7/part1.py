file = open("input.txt", "r")
hands = list(map(lambda x: x.rstrip("\n"), file.readlines()))
file.close()

def rank_hand(cards):
    pattern = []
    scards = sorted(cards) # duplicates will be adjacent
    prev = None
    for i in range(len(scards)):
        if scards[i] == prev:
            pattern[-1] += 1
        else:
            pattern.append(1)
        prev = scards[i]
    pattern.sort(reverse=True)
    if pattern[0] == 5:
        return 7
    elif pattern[0] == 4:
        return 6
    elif pattern[0] == 3 and pattern[1] == 2:
        return 5
    elif pattern[0] == 3:
        return 4
    elif pattern[0] == 2 and pattern[1] == 2:
        return 3
    elif pattern[0] == 2:
        return 2
    else:
        return 1

def get_card_num(card):
    if card == "A":
        return 12
    elif card == "K":
        return 11
    elif card == "Q":
        return 10
    elif card == "J":
        return 9
    elif card == "T":
        return 8
    else:
        return int(card) - 2

# treat hand as a base 13 number
def get_tiebreaker(cards):
    multiplier = 1
    tiebreaker = 0
    for i in range(len(cards) - 1, -1, -1):
        tiebreaker += get_card_num(cards[i]) * multiplier
        multiplier *= 13
    return tiebreaker

class Hand:
    def __init__(self, cards, bid):
        self.cards = cards
        self.bid = bid
        self.rank = rank_hand(cards)
        self.tiebreak = get_tiebreaker(cards)

def convert_hand_from_string(s: str):
    h = s.split(" ")
    return Hand(h[0], int(h[1]))

hands = list(map(lambda x: convert_hand_from_string(x), hands))
hands.sort(key=lambda x: x.rank * (10 ** 8) + x.tiebreak)

total_winnings = 0
for i in range(len(hands)):
    total_winnings += hands[i].bid * (i + 1)
print(total_winnings)
