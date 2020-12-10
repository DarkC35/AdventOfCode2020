from timeit import default_timer as timer
import numpy as np


def xmas(numbers, preamble):
    for i in range(preamble, len(numbers)):
        for x in range(1, preamble):
            for y in range(x+1, preamble+1):
                if numbers[i] == (numbers[i-x] + numbers[i-y]):
                    break
            else:
                continue
            break
        else:
            invalid_number = numbers[i]
            result_tuple = None
            for j in range(0, i-1):
                sum = numbers[j]
                for k in range(j+1, i):
                    if sum + numbers[k] <= invalid_number:
                        sum += numbers[k]
                        if sum == invalid_number:
                            result_tuple = (numbers[j], numbers[k])
                            break
                    else:
                        break
                if result_tuple == None:
                    continue
                else:
                    break
            return result_tuple


start = timer()
with open("input.txt") as file:
    numbers = [int(line) for line in file]
smallest, largest = xmas(numbers, 25)
result = smallest + largest
end = timer()
print("Result: ", result)
print("Time (in sec): ", end-start)
