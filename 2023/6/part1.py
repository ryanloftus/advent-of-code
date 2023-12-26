times = [53, 89, 76, 98]
distances = [313, 1090, 1214, 1201]

ways_to_win_product = 1
for i in range(len(times)):
    ways_to_win = 0
    for j in range(times[i]+1):
        if j * (times[i] - j) >= distances[i]:
            ways_to_win += 1
    ways_to_win_product *= ways_to_win
print(ways_to_win_product)
