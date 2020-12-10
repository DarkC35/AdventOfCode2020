from timeit import default_timer as timer


start = timer()
x = 0
count = 0
with open("input.txt", "r") as file:
    for i, line in enumerate(file):
        if i != 0:
            if line[x] == "#":
                count += 1
        x = (x + 3) % (len(line)-1)
end = timer()
print("Count: ", count)
print("Time (in sec): ", end-start)
