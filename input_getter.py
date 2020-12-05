def get_input(filename='input.txt') -> list:
    return_list: list = []
    with open(filename, 'rt') as inputfile:
        for line in inputfile.readlines():
            return_list.append(line)
    return return_list
