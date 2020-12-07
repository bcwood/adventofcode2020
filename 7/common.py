bags = {}

def get_bags():
    with open("7/input.txt", "r") as file:
        data = file.read().split('\n')

    for line in data:
        parts = line.split(" contain ")
        color = parts[0].replace(" bags", "")
        
        contains = []

        if parts[1] != "no other bags.":
            contains_bags = parts[1].split(", ")
            for c in contains_bags:
                parts = c.split(" ")
                num = int(parts[0])
                color_name = f"{parts[1]} {parts[2]}"
                contains.append((num, color_name))

        bags[color] = contains
    
    return bags