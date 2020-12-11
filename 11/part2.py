import copy

def get_next_seat_state(x, y):
    state = get_seat(x, y)    
    if state == ".":
        return "."
    
    occupied = count_visible_occupied(x, y)

    if state == "L" and occupied == 0:
        return "#"            
    elif state == "#" and occupied >= 5:
        return "L"
    else:
        return state

def count_visible_occupied(x, y):
    count = 0
    count += search_direction(x, y, 0, -1) # N
    count += search_direction(x, y, 1, -1) # NE
    count += search_direction(x, y, 1, 0) # E
    count += search_direction(x, y, 1, 1) # SE
    count += search_direction(x, y, 0, 1) # S
    count += search_direction(x, y, -1, 1) # SW
    count += search_direction(x, y, -1, 0) # W
    count += search_direction(x, y, -1, -1) # NW
    
    return count

def search_direction(x, y, dx, dy):    
    x += dx
    y += dy    

    while in_range(x, y):
        state = get_seat(x, y)
        if state == "#":
            return 1
        elif state == "L":
            return 0

        x += dx
        y += dy

    return 0

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
