from copy import copy


def get_input() -> list:
    numbers: list = []
    with open('input.txt', 'rt') as inputfile:
        for line in inputfile.readlines():
            numbers.append(int(line))
    return numbers


if __name__ == '__main__':
    num_list = get_input()
    num_list_copy = copy(num_list)

    for num0 in num_list:
        num_list_copy.pop()
        num_list_copy2 = copy(num_list_copy)
        for num1 in num_list_copy:
            num_list_copy2.pop()
            for num2 in num_list_copy2:
                if num0 + num1 + num2 == 2020:
                    print(f"{num0} + {num1} + {num2} = 2020")
                    print(f"{num0} * {num1} * {num2} = {num0*num1*num2}")
                    exit()
