from common import *

with open("4/input.txt", "r") as file:
    data = file.read().split('\n\n')

count = 0

for passport in data:
    if has_req_fields(passport):
        count += 1

print(count)
