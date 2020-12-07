with open("6/input.txt", "r") as file:
    data = file.read().split('\n\n')

count = 0

for group in data:
    group = group.replace('\n', "") # get all fields onto one line

    chars = []

    for c in group:
        if not c in chars:
            chars.append(c)
            count += 1

print(count)
