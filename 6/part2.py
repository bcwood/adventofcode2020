def intersect(a, b):
    return list(set(a) & set(b))

with open("6/input.txt", "r") as file:
    data = file.read().split('\n\n')

count = 0

for group in data:
    lines = group.split('\n')
    common = lines[0]

    for line in lines:
        common = intersect(common, line)

    count += len(common)    

print(count)
