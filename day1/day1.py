import copy


def get_input() -> list:
    numbers: list = []
    with open('input.txt', 'rt') as inputfile:
        for line in inputfile.readlines():
            numbers.append(int(line))
    return numbers


def find_2020(numb: int, comp_num_list: []) -> int:
    for c_num in comp_num_list:
        if c_num + numb == 2020:
            print(f"{c_num} + {numb} = 2020")
            return c_num
    return 0


if __name__ == '__main__':
    num_list = get_input()
    num_list_copy = copy.copy(num_list)

    for num in num_list:
        num_list_copy.pop()
        res = find_2020(num, num_list_copy)
        if res:
            print(f"{num} * {res} = {num*res}")
            break

