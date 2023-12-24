file = open("input.txt", "r")
lines = file.readlines()
file.close()

string_digits = [
    ("one", 1),
    ("two", 2),
    ("three", 3),
    ("four", 4),
    ("five", 5),
    ("six", 6),
    ("seven", 7),
    ("eight", 8),
    ("nine", 9),
]

def is_start_of_string_digit(line: str, i: int):
    for k, v in string_digits:
        if i + len(k) < len(line) and line[i:i+len(k)] == k:
            return (True, v)
    return (False, None)

def find_first_digit(line: str):
    for i in range(len(line)):
        if line[i].isdigit():
            return int(line[i])
        is_string_dig, dig = is_start_of_string_digit(line, i)
        if is_string_dig:
            return dig

def find_last_digit(line: str):
    for i in range(len(line) - 1, -1, -1):
        if line[i].isdigit():
            return int(line[i])
        is_string_dig, dig = is_start_of_string_digit(line, i)
        if is_string_dig:
            return dig

calibration_values = map(lambda x: find_first_digit(x) * 10 + find_last_digit(x), lines)
calibration_sum = sum(calibration_values)
print(calibration_sum)
