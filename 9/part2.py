def find_value_in_range(num_vals, target):
    for i in range(0, len(data) - num_vals):
        total = 0
        low = 99999999
        high = 0

        for j in range(i, i + num_vals):
            value = int(data[j])
            total += value
            
            if value < low:
                low = value
            if value > high:
                high = value            
        
        if total == target:
            print(f"{low + high}")
            return True

    return False

with open("9/input.txt", "r") as file:
    data = file.read().split('\n')

num_vals = 2
while True:
    if find_value_in_range(num_vals, 675280050):
        break

    num_vals += 1
