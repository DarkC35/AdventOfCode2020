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
            return numbers[i]


start = timer()
with open("input.txt") as file:
    numbers = [int(line) for line in file]
result = xmas(numbers, 25)
end = timer()
print("Result: ", result)
print("Time (in sec): ", end-start)
