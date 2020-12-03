with open("3/input.txt", "r") as file:
    data = file.read().split('\n')

def collisions(data, dx, dy):
    height = len(data)
    width = len(data[0])
    x = 0
    count = 0

    for y in range(0, height, dy):
        if (data[y][x] == "#"):
            count += 1
        
        x = (x + dx) % width
    
    return count

# part 1
print(collisions(data, 3, 1))

# part 2
print(collisions(data, 1, 1) * 
      collisions(data, 3, 1) * 
      collisions(data, 5, 1) * 
      collisions(data, 7, 1) * 
      collisions(data, 1, 2))