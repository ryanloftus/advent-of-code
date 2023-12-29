file = open("input.txt", "r")
lines = list(map(lambda x: x.rstrip("\n"), file.readlines()))
file.close()

steps = lines[0].split(",")

def holiday_ascii_string_helper(s: str):
    h = 0
    for c in s:
        h = ((h + ord(c)) * 17) % 256
    return h

hashes = map(lambda x: holiday_ascii_string_helper(x), steps)
hash_sum = sum(hashes)
print(hash_sum)
