from timeit import default_timer as timer


def check_for_infinity_loop(lines, index_of_altered_instruction):
    already_executed_indices = set()
    curr_index = 0
    acc = 0
    while curr_index not in already_executed_indices and curr_index < len(lines):
        already_executed_indices.add(curr_index)
        instruction, number = lines[curr_index].split(" ")
        if instruction == "nop":
            if curr_index == index_of_altered_instruction:
                curr_index += int(number)
            else:
                curr_index += 1
        elif instruction == "acc":
            acc += int(number)
            curr_index += 1
        elif instruction == "jmp":
            if curr_index == index_of_altered_instruction:
                curr_index += 1
            else:
                curr_index += int(number)
    is_infinity_loop = curr_index != len(lines)
    return is_infinity_loop, acc


start = timer()
with open("input.txt", "r") as file:
    lines = [line.strip() for line in file.readlines()]
# so brute force it will be
for i, line in enumerate(lines):
    instruction, _ = line.split(" ")
    if instruction in {"jmp", "nop"}:
        is_infinity_loop, acc = check_for_infinity_loop(lines, i)
        if is_infinity_loop == False:
            break
end = timer()
print("Result: ", acc)
print("Time (in sec): ", end-start)