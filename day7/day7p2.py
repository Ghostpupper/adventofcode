import re

from input_getter import get_input

bags = []
colors = []
counter = 0
cur_color = ""
regex1 = r"(.*)bags contain (.*)."
regex2 = r"((\d*) (\w* \w*) bag)"

class Bag:
    def __init__(self, color):
        self.slots: int = 0
        self.color: str = color.rstrip(' ')
        self.other_bags = {}
        self.gold_inside = False

    def add_other_bag(self, color: str, no: int):
        color = color.rstrip(' ')
        self.other_bags[color] = no
        self.slots += no
        if color == "shiny gold":
            self.gold_inside = True


def find_self(input_txt):
    found = re.findall(regex1, input_txt)
    if found:
        self_color = found[0][0]
        other_bags_str = found[0][1]
        return self_color, other_bags_str
    else:
        return "", ""

def find_other(other_str):
    if "no other" in other_str:
        return 0, ""
    while re.search(regex2, other_str):
        match = re.findall(regex2, other_str)[0]
        full_str = match[0]
        no = int(match[1])
        color = match[2]
        other_str = other_str.replace(full_str, '')
        yield no, color
    return

def get_bag(input_txt: str) -> Bag:
    s_color, other_bags = find_self(input_txt)
    new_bag = Bag(s_color)
    for num, o_color in find_other(other_bags):
        if num:
            new_bag.add_other_bag(o_color, num)
    return new_bag

def retrive_bag(color: str):
    for bag in bags:
        if bag.color == color:
            return bag

def check_inception_inner(i_bag):
    if i_bag.other_bags:
        for bag_c in i_bag.other_bags.keys():
            bag = retrive_bag(bag_c)
            if bag.other_bags:
                return True
    return False

def count_inner_b(start_bag, times=1):
    global counter
    if not start_bag.slots or start_bag.gold_inside:
        return
    if start_bag.color == "shiny gold":
        start_bag.gold_inside = True
    for i_bag_c, i_count in start_bag.other_bags.items():
        i_bag = retrive_bag(i_bag_c)
        counter += i_count*times
        if not check_inception_inner(i_bag):
            counter += i_count * i_bag.slots * times
            print(f"{i_count} * {i_bag.slots} * {times}")
        else:
            count_inner_b(i_bag, times=i_bag.slots*times)

if __name__ == '__main__':

    in_txt = get_input()

    for line in in_txt:
        found_bag = get_bag(line)
        bags.append(found_bag)
        colors.append(found_bag.color)

    start_color = "shiny gold"
    start_bag = retrive_bag(start_color)
    count_inner_b(start_bag)

    print(f"{counter}")
