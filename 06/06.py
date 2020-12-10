from timeit import default_timer as timer


def count_trees(input_lines, right, down):
    x = 0
    count = 0
    for i, line in enumerate(input_lines):
        if i % down != 0:
            continue
        if i != 0:
            if line[x] == "#":
                count += 1
        x = (x + right) % (len(line)-1)
    return count


start = timer()
with open("input.txt", "r") as file:
    lines = file.readlines()
slope_1 = count_trees(lines, 1, 1)
slope_2 = count_trees(lines, 3, 1)
slope_3 = count_trees(lines, 5, 1)
slope_4 = count_trees(lines, 7, 1)
slope_5 = count_trees(lines, 1, 2)
end = timer()
print("Result: ", slope_1 * slope_2 * slope_3 * slope_4 * slope_5)
print("Time (in sec): ", end-start)
