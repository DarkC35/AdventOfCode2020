from timeit import default_timer as timer


def calculate_direction_index_after_rotation(old_index, direction, degrees):
    if direction == "R":
        return (old_index + (degrees//90)) % 4
    elif direction == "L":
        return (old_index - (degrees//90)) % 4


start = timer()
north_south_position = 0
east_west_position = 0
with open("input.txt") as file:
    instructions = [(line[0], int(line[1:])) for line in file]
directions = ["N", "E", "S", "W"]
current_direction_index = 1
for action, value in instructions:
    if action in ["R", "L"]:
        current_direction_index = calculate_direction_index_after_rotation(
            current_direction_index, action, value
        )
    if action == "F":
        action = directions[current_direction_index]
    if action == "N":
        north_south_position += value
    elif action == "S":
        north_south_position -= value
    elif action == "E":
        east_west_position += value
    elif action == "W":
        east_west_position -= value
result = abs(north_south_position) + abs(east_west_position)
end = timer()
print("Result: ", result)
print("Time (in sec): ", end-start)
