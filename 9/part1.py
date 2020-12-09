def is_valid_value(index):
    global preamble
    target = int(data[index])
    
    for i in range(index - preamble, index - 1):
        for j in range(i + 1, index):
            val1 = int(data[i])
            val2 = int(data[j])
            if val1 + val2 == target:
                return True

    return False

preamble = 25

with open("9/input.txt", "r") as file:
    data = file.read().split('\n')

for i in range(preamble, len(data)):
    if not is_valid_value(i):
        print(data[i])
        break
