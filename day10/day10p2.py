from copy import copy

from input_getter import get_input, get_input_int

dif_range = 3

def report_built_in(number: int):
    global dif_range
    print(f"Built in adapter is: {number + dif_range} ")
    built_in = number + dif_range
    return built_in

def find_built_in(in_ints):
    for i, val in enumerate(in_ints):
        if i == len(in_ints) - 1:
            return report_built_in(val)

        sub_res = in_ints[i + 1] - in_ints[i]
        if sub_res > dif_range:
            return report_built_in(val)


if __name__ == '__main__':
    in_ints = get_input_int('i2.txt')
    in_ints.sort()
    in_ints.insert(0, 0)
    in_ints.append(find_built_in(in_ints))
    print(in_ints)
    print(len(in_ints))
    print(pow(3, len(in_ints)))
