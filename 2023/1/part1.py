file = open("input.txt", "r")
lines = file.readlines()
file.close()

def find_first_digit(line):
    for c in line:
        if c.isdigit():
            return int(c)

def find_last_digit(line):
    for i in range(len(line) - 1, -1, -1):
        if line[i].isdigit():
            return int(line[i])

calibration_values = map(lambda x: find_first_digit(x) * 10 + find_last_digit(x), lines)
calibration_sum = sum(calibration_values)
print(calibration_sum)
