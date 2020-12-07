from timeit import default_timer as timer


start = timer()
result = 0
with open("input.txt", "r") as file:
    line = file.readline()
    while line != "":
        questions_answered_with_yes = set()
        while line != "\n" and line != "":
            questions_answered_with_yes.update(set(line.strip()))
            line = file.readline()
        result += len(questions_answered_with_yes)
        line = file.readline()
end = timer()
print("Result: ", result)
print("Time (in sec): ", end-start)