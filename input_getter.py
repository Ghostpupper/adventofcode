def get_input(filename='input.txt') -> list:
    return_list: list = []
    with open(filename, 'rt') as inputfile:
        for line in inputfile.readlines():
            return_list.append(line)
    return return_list

def get_input_int(filename='input.txt') -> list:
    return_list: list = []
    with open(filename, 'rt') as inputfile:
        for line in inputfile.readlines():
            return_list.append(int(line))
    return return_list
