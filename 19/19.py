from timeit import default_timer as timer


start = timer()
with open("input.txt") as file:
    adapters = sorted([int(line) for line in file])
current_jolts = 0
count_1_jolt_difference = 0
count_3_jolt_difference = 0
for adapter in adapters:
    if adapter - current_jolts == 1:
        count_1_jolt_difference += 1
    elif adapter - current_jolts == 3:
        count_3_jolt_difference += 1
    else:
        print(adapter - current_jolts)
    current_jolts = adapter
count_3_jolt_difference += 1
result = count_1_jolt_difference * count_3_jolt_difference
end = timer()
print("Result: ", result)
print("Time (in sec): ", end-start)
