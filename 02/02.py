from timeit import default_timer as timer
# Version 1
start = timer()
with open("input.txt", "r") as f:
    numbers = [int(x) for x in f]
result = 0
for x in numbers:
    for y in numbers:
        for z in numbers:
            if (x + y + z) == 2020:
                #print("x*y*z=", (x*y*z), x, y, z)
                result = (x*y*z)
                break
        else:
            continue
        break
    else:
        continue
    break
end = timer()
print("Result: ", result)
print("Time (in sec): ", end-start)

# Version 2 (Dani)
start = timer()
with open("input.txt", "r") as f:
    numbers = [int(x) for x in f]
result = 0
for x in range(0, len(numbers)-2):
    for y in range(x+1, len(numbers)-1):
        for z in range(y+1, len(numbers)):
            if (numbers[x] + numbers[y] + numbers[z]) == 2020:
                result = (numbers[x] * numbers[y] * numbers[z])
                break
        else:
            continue
        break
    else:
        continue
    break
end = timer()
print("Result: ", result)
print("Time (in sec): ", end-start)
