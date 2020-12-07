from common import *

possible = set()

def check_bag(root, bag, color):
    global possible
    contains = bags[bag]
    
    for contains_bag in contains:
        if contains_bag[1] == color:
            possible.add(root)
            break
        else:
            check_bag(root, contains_bag[1], color)

bags = get_bags()

for index, bag in enumerate(bags):
    check_bag(bag, bag, "shiny gold")

print(len(possible))
