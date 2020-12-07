from common import *

def count_bags(color):
    count = 1
    contains = bags[color]
    
    for contains_bag in contains:
        count += contains_bag[0] * count_bags(contains_bag[1])

    return count

bags = get_bags()

print(count_bags("shiny gold") - 1)
