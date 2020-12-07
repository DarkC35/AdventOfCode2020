from timeit import default_timer as timer
import re


def get_set_of_all_holding_bags_for(search_string, bag_dict):
    holding_bag = set()
    for key, bag_list in bag_dict.items():
        for bag_color, _ in bag_list:
            if bag_color == search_string:
                holding_bag |= {key}
    for bag in set(holding_bag):
        holding_bag |= get_set_of_all_holding_bags_for(bag, bag_dict)
    return holding_bag


start = timer()
bag_dict = {}
contain_regex_object = re.compile(r'(\w+ \w+) bags contain ((no other bags)|((\d+ \w+ \w+ bags?)(, \d+ \w+ \w+ bags?)*)).')
bag_regex_object = re.compile(r'(\d+) (\w+ \w+) bags?')
with open("input.txt", "r") as file:
    for line in file:
        contained_bags = []
        contain_match_object = contain_regex_object.match(line)
        if(contain_match_object.group(2) != "no other bags"):
            contained_bags = [(bag_regex_object.match(bag_string.strip()).group(2), int(bag_regex_object.match(bag_string.strip()).group(1))) for bag_string in contain_match_object.group(2).split(',')]
        bag_dict[contain_match_object.group(1)] = contained_bags
bags_that_can_contain_shiny_gold_bag = get_set_of_all_holding_bags_for("shiny gold", bag_dict)
end = timer()
print("Result: ", len(bags_that_can_contain_shiny_gold_bag))
print("Time (in sec): ", end-start)