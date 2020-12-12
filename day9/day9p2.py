sum = 1124361034

def get_input(filename='input.txt') -> list:
    return_list: list = []
    with open(filename, 'rt') as inputfile:
        for line in inputfile.readlines():
            return_list.append(int(line))
    return return_list

if __name__ == '__main__':
    numbers = get_input()
