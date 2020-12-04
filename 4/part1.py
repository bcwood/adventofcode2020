with open("4/input.txt", "r") as file:
    data = file.read().split('\n\n')

def has_req_fields(passport):
    for req in ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]:
        if not f"{req}:" in passport:
            return False
    
    return True

count = 0

for passport in data:
    if has_req_fields(passport):
        count += 1

print(count)
