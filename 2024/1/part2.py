from collections import Counter

list1 = []
list2 = []

with open("input.txt") as f:
    for line in f.readlines():
        split_line = line.split("   ")
        list1.append(int(split_line[0]))
        list2.append(int(split_line[1]))

list2_counts = Counter(list2)

similarity_score = 0
for n in list1:
    similarity_score += n * list2_counts[n]

print(similarity_score)
