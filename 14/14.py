from timeit import default_timer as timer
import re


def get_count_of_bags_inside_of(search_string, bag_dict):
    count = 0
    for bag_color, quantity in bag_dict[search_string]:
        count += quantity + \
            (quantity * get_count_of_bags_inside_of(bag_color, bag_dict))
    return count


start = timer()
bag_dict = {}
contain_regex_object = re.compile(
    r'(\w+ \w+) bags contain ((no other bags)|((\d+ \w+ \w+ bags?)(, \d+ \w+ \w+ bags?)*)).')
bag_regex_object = re.compile(r'(\d+) (\w+ \w+) bags?')
with open("input.txt", "r") as file:
    for line in file:
        contained_bags = []
        contain_match_object = contain_regex_object.match(line)
        if(contain_match_object.group(2) != "no other bags"):
            contained_bags = [
                (
                    bag_regex_object.match(bag_string.strip()).group(2),
                    int(bag_regex_object.match(bag_string.strip()).group(1))
                )
                for bag_string in contain_match_object.group(2).split(',')
            ]
        bag_dict[contain_match_object.group(1)] = contained_bags
result = get_count_of_bags_inside_of("shiny gold", bag_dict)
end = timer()
print("Result: ", result)
print("Time (in sec): ", end-start)
