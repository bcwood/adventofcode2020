import copy

def get_next_seat_state(x, y):
    state = get_seat(x, y)    
    if state == ".":
        return "."
    
    occupied = count_adjacent_occupied(x, y)

    if state == "L" and occupied == 0:
        return "#"            
    elif state == "#" and occupied >= 4:
        return "L"
    else:
        return state

def count_adjacent_occupied(x, y):
    count = 0
    for x2 in range(x - 1, x + 2):
        for y2 in range(y - 1, y + 2):
            if x2 == x and y2 == y:
                continue
            if get_seat(x2, y2) == "#":
                count += 1

    return count

def get_seat(x, y):
    # treat seats out of boundaries as the floor
    if not in_range(x, y):
        return "."
    
    return current[y][x]

def in_range(x, y):
    return x >= 0 and x < width and y >= 0 and y < height

with open("11/input.txt", "r") as file:
    data = file.read().split('\n')

# transform each line into array of chars
current = []
for line in data:
    current.append(list(line))

next = copy.deepcopy(current)
height = len(current)
width = len(current[0])

# continue until state hasn't changed
while True:
    for x in range(0, width):
        for y in range(0, height):
            next[y][x] = get_next_seat_state(x, y)
    
    if next == current:
        break

    current = copy.deepcopy(next)

# count occupied seats
count = 0
for x in range(0, width):
    for y in range(0, height):
        if current[y][x] == "#":
            count += 1

print(count)
