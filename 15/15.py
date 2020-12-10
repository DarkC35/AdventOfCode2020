from timeit import default_timer as timer


start = timer()
with open("input.txt", "r") as file:
    lines = [line.strip() for line in file.readlines()]
already_executed_indices = set()
acc = 0
curr_index = 0
while curr_index not in already_executed_indices:
    already_executed_indices.add(curr_index)
    instruction, number = lines[curr_index].split(" ")
    if instruction == "nop":
        curr_index += 1
    elif instruction == "acc":
        acc += int(number)
        curr_index += 1
    elif instruction == "jmp":
        curr_index += int(number)
end = timer()
print("Result: ", acc)
print("Time (in sec): ", end-start)
