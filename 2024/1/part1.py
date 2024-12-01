list1 = []
list2 = []

with open("input.txt") as f:
    for line in f.readlines():
        split_line = line.split("   ")
        list1.append(int(split_line[0]))
        list2.append(int(split_line[1]))
    
list1.sort()
list2.sort()

diffs = [abs(list1[i]-list2[i]) for i in range(len(list1))]
total_diff = sum(diffs)
print(total_diff)
