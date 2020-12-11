count1 = 0
count3 = 0

def count_diff(val1, val2):
    global count1
    global count3
    diff = val2 - val1
    
    if diff == 3:
        count3 += 1
    elif diff == 1:
        count1 += 1

data = sorted([int(x.strip()) for x in open("10/input.txt")] + [0])

for i in range(len(data) - 1):    
    count_diff(data[i], data[i + 1])

# add final diff of 3 jolts to device
count3 += 1
    
print(count1 * count3)
