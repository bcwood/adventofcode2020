count = 0

for line in open("2/input.txt", "r"):
    parts = line.split(" ")
    positions = parts[0]
    pos1 = int(positions.split("-")[0]) - 1
    pos2 = int(positions.split("-")[1]) - 1
    letter = parts[1][0]
    text = parts[2]

    if (bool(text[pos1] == letter) ^ bool(text[pos2] == letter)):
        count += 1

print(count)
