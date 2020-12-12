from timeit import default_timer as timer


start = timer()
north_south_waypoint = 1
east_west_waypoint = 10
north_south_position = 0
east_west_position = 0
with open("input.txt") as file:
    instructions = [(line[0], int(line[1:])) for line in file]
for action, value in instructions:
    if action in ["R", "L"]:
        temp = north_south_waypoint
        if (action == "R" and value == 90) or (action == "L" and value == 270):
            north_south_waypoint = east_west_waypoint * (-1)
            east_west_waypoint = temp
        elif value == 180:
            north_south_waypoint *= (-1)
            east_west_waypoint *= (-1)
        elif (action == "R" and value == 270) or (action == "L" and value == 90):
            north_south_waypoint = east_west_waypoint
            east_west_waypoint = temp * (-1)
    if action == "F":
        north_south_position += (north_south_waypoint * value)
        east_west_position += (east_west_waypoint * value)
    if action == "N":
        north_south_waypoint += value
    elif action == "S":
        north_south_waypoint -= value
    elif action == "E":
        east_west_waypoint += value
    elif action == "W":
        east_west_waypoint -= value
result = abs(north_south_position) + abs(east_west_position)
end = timer()
print("Result: ", result)
print("Time (in sec): ", end-start)
