from timeit import default_timer as timer


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
        passport_fields = {
            entry.split(":")[0] for entry in passport_string.split(" ")
        }
        if passport_fields.issuperset(required_fields):
            count += 1
        line = file.readline()
end = timer()
print("Result: ", count)
print("Time (in sec): ", end-start)
