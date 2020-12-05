def get_input() -> list:
    return_list: list = []
    with open('input.txt', 'rt') as inputfile:
        for line in inputfile.readlines():
            return_list.append(line)
    return return_list
