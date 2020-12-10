from timeit import default_timer as timer


# not efficient (takes some hours)
def count_arrangements_not_efficient(adapters, current_jolts):
    compatible_adapter_indexes = [i for i, x in enumerate(adapters[0:3]) if x <= current_jolts + 3]
    if len(compatible_adapter_indexes) ==  0:
        return 1
    count = 0
    for index in compatible_adapter_indexes:
        count += count_arrangements_not_efficient(adapters[index+1:], adapters[index])
    return count


# solution with caching! (thx Dani & Ginzi)
def count_arrangements(adapters, current_jolts, cache):
    compatible_adapter_indexes = [i for i, x in enumerate(adapters[0:3]) if x <= current_jolts + 3]
    if len(compatible_adapter_indexes) ==  0:
        return 1
    cached = cache.get(current_jolts)
    if cached:
        return cached
    count = 0
    for index in compatible_adapter_indexes:
        result = count_arrangements(adapters[index+1:], adapters[index], cache)
        count += result
    cache[current_jolts] = count
    return count


start = timer()
cache = {}
with open("input.txt") as file:
    adapters = sorted([int(line) for line in file])
result = count_arrangements(adapters, 0, cache)
end = timer()
print("Result: ", result)
print("Time (in sec): ", end-start)