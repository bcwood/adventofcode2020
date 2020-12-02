import re

count = 0

for line in open("2/input.txt", "r"):
    parts = line.split(" ")
    occurs = parts[0]
    occursMin = int(occurs.split("-")[0])
    occursMax = int(occurs.split("-")[1])
    letter = parts[1][0]
    text = parts[2]

    matches = re.findall(letter, text)

    if (len(matches) >= occursMin and len(matches) <= occursMax):
        count += 1

print(count)
