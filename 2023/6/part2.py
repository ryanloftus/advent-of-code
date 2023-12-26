time = 53897698
distance = 313109012141201

ways_to_win = 0
for j in range(time+1):
    if j * (time - j) >= distance:
        ways_to_win += 1
print(ways_to_win)
