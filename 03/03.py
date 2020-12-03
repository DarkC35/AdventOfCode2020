import re
from timeit import default_timer as timer


def validate_password(password, letter, min, max):
    occurrences = len([m.start() for m in re.finditer(letter, password)])
    return occurrences >= min and occurrences <= max


start = timer()
count = 0
reg_obj = re.compile(r'(\d+)-(\d+) (.): (.+)')
with open("input.txt", "r") as file:
    for line in file:
        result = reg_obj.search(line)
        if validate_password(result.group(4), result.group(3), int(result.group(1)), int(result.group(2))):
            count += 1
end = timer()
print("Count: ", count)
print("Time (in sec): ", end-start)
