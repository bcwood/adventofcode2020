import re

def has_req_fields(passport):
    for req in ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]:
        if not f"{req}:" in passport:
            return False
    
    return True

def valid_range(value, min, max):
    return int(value) >= min and int(value) <= max

def valid_birthyear(value):
    return valid_range(value, 1920, 2002)

def valid_issueyear(value):
    return valid_range(value, 2010, 2020)

def valid_expiration(value):
    return valid_range(value, 2020, 2030)

def valid_height(value):
    if value.endswith("cm"):
        value = value[0:len(value)-2]
        return valid_range(value, 150, 193)
    elif value.endswith("in"):
        value = value[0:len(value)-2]
        return valid_range(value, 59, 76)
    else:
        return False
    
def valid_haircolor(value):
    return re.search("#[0-9a-f]{6}", value)

def valid_eyecolor(value):
    return re.search("amb|blu|brn|gry|grn|hzl|oth", value)

def valid_passportid(value):
    return re.search("^[0-9]{9}$", value)

with open("4/input.txt", "r") as file:
    data = file.read().split('\n\n')

required = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
count = 0

for passport in data:
    passport = passport.replace('\n', " ") # get all fields onto one line
    
    if not has_req_fields(passport):
        continue

    fields = passport.split(" ")
    
    fieldDict = {} # build dictionary of fields
    for field in fields:
        parts = field.split(":")
        fieldDict[parts[0]] = parts[1]
    
    if (valid_birthyear(fieldDict["byr"]) and
        valid_issueyear(fieldDict["iyr"]) and
        valid_expiration(fieldDict["eyr"]) and
        valid_height(fieldDict["hgt"]) and
        valid_haircolor(fieldDict["hcl"]) and
        valid_eyecolor(fieldDict["ecl"]) and
        valid_passportid(fieldDict["pid"])):

        count += 1

print(count)
