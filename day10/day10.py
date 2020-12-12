from copy import copy

from input_getter import get_input, get_input_int

dif_range = 3
dif_dict = {}
for i in range(1, dif_range+1):
    dif_dict[i] = 0

def report_built_in(number: int):
    global dif_dict, dif_range
    print(f"Built in adapter is: {number + dif_range} ")
    print(f"{number + dif_range} - {number} = {dif_range}")
    dif_dict[dif_range] += 1

    for key in dif_dict.keys():
        if dif_dict[key]:
            print(f"There are {dif_dict[key]} of {key} jolt/s")
    res = dif_dict[1]*dif_dict[dif_range]
    print(f"{dif_dict[1]} * {dif_dict[dif_range]} = {res}")

if __name__ == '__main__':
    in_ints = get_input_int()
    in_ints.sort()
    in_ints.insert(0, 0)

    for i, val in enumerate(in_ints):
        if i == len(in_ints) - 1:
            report_built_in(val)
            break

        sub_res = in_ints[i + 1] - in_ints[i]
        print(f"{in_ints[i + 1]} - {in_ints[i]} = {sub_res}")
        if sub_res > dif_range:
            report_built_in(val)
            break
        dif_dict[sub_res] += 1