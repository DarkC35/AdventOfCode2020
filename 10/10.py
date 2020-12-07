from timeit import default_timer as timer


def rec_place_finder(search_string, lower_half, upper_half, lower_half_indicator, upper_half_indicator):
    if len(search_string) == 1:
        if search_string[0] == lower_half_indicator:
            return lower_half
        elif search_string[0] == upper_half_indicator:
            return upper_half
    elif search_string[0] == lower_half_indicator:
        return rec_place_finder(search_string[1:len(search_string)], lower_half, upper_half - ((upper_half + 1 - lower_half) // 2), lower_half_indicator, upper_half_indicator)
    elif search_string[0] == upper_half_indicator:
        return rec_place_finder(search_string[1:len(search_string)], lower_half + ((upper_half + 1 - lower_half) // 2), upper_half, lower_half_indicator, upper_half_indicator)
    return


start = timer()
ids = []
with open("input.txt", "r") as file:
    for line in file:
        row = rec_place_finder(line[0:7], 0, 127, "F", "B")
        column = rec_place_finder(line[7:10], 0, 7, "L", "R")
        ids.append((row * 8) + column)
sorted_ids = sorted(ids)
result = 0
prev = sorted_ids[0] - 1
for x in sorted_ids:
    if x == (prev + 1):
        prev = x
    else:
        result = (x - 1)
        break
end = timer()
print("Result: ", result)
print("Time (in sec): ", end-start)
