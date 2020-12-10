from timeit import default_timer as timer
import re


def height_validate(height_string):
    match_object = re.match(r'(\d+)(cm|in)', height_string)
    return match_object and ((match_object.group(2) == "cm" and 150 <= int(match_object.group(1)) <= 193) or (match_object.group(2) == "in" and 59 <= int(match_object.group(1)) <= 76))


def validate_dict(passport_dict):
    return passport_dict["byr"].isdigit() and 1920 <= int(passport_dict["byr"]) <= 2002 and len(passport_dict["byr"]) == 4 and \
        passport_dict["iyr"].isdigit() and 2010 <= int(passport_dict["iyr"]) <= 2020 and len(passport_dict["iyr"]) == 4 and \
        passport_dict["eyr"].isdigit() and 2020 <= int(passport_dict["eyr"]) <= 2030 and len(passport_dict["eyr"]) == 4 and \
        height_validate(passport_dict["hgt"]) and \
        re.match(r'#[0-9a-f]{6}', passport_dict["hcl"]) and \
        passport_dict["ecl"] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"] and \
        len(passport_dict["pid"]) == 9 and passport_dict["pid"].isdigit()


start = timer()
required_fields = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
count = 0
with open("input.txt", "r") as file:
    line = file.readline()
    while line != "":
        passport_string = ""
        while line != "\n" and line != "":
            passport_string += line.replace("\n", " ")
            line = file.readline()
        passport_string = passport_string.strip()
        passport_fields = {entry.split(":")[0]
                           for entry in passport_string.split(" ")}
        passport_dict = {entry.split(":")[0]: entry.split(
            ":")[1] for entry in passport_string.split(" ")}
        if set(passport_dict.keys()).issuperset(required_fields):
            if validate_dict(passport_dict):
                count += 1
        line = file.readline()
end = timer()
print("Result: ", count)
print("Time (in sec): ", end-start)
