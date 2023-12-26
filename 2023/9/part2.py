file = open("input.txt", "r")
lines = list(map(lambda x: x.rstrip("\n"), file.readlines()))
file.close()


def all_zeros(nums):
    for num in nums:
        if num != 0:
            return False
    return True


extrapolated_values = []
for line in lines:
    history = []
    history.append(list(map(lambda x: int(x), line.split(" "))))
    while not all_zeros(history[-1]):
        history.append([])
        for i in range(len(history[-2]) - 1):
            history[-1].append(history[-2][i+1] - history[-2][i])
    prediction = [0] * len(history)
    for i in range(len(history) - 2, -1, -1):
        prediction[i] = history[i][0] - prediction[i+1]
    extrapolated_values.append(prediction[0])

print(sum(extrapolated_values))
