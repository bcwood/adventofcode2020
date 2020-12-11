from collections import Counter

data = sorted([int(line.strip()) for line in open("10/input.txt")] + [0])
count = Counter({0:1})

for i in data:
    for j in range(i + 1, i + 4):
        count[j] += count[i]

print(count[max(data) + 3])
