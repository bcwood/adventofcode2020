from common import *

with open("4/input.txt", "r") as file:
    data = file.read().split('\n\n')

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
