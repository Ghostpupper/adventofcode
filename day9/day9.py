preample = 25

def get_input(filename='input.txt') -> list:
    return_list: list = []
    with open(filename, 'rt') as inputfile:
        for line in inputfile.readlines():
            return_list.append(int(line))
    return return_list

def check_XMAS_valid(index: int, nums: list):
    adds_to = nums[index]
    numbers_to_comp = nums[index - preample:index]
    for c_num in numbers_to_comp:
        subtraction = adds_to - c_num
        if subtraction == c_num or subtraction < 1:
            continue
        if subtraction in numbers_to_comp:
            print(f"{subtraction} + {c_num} = {adds_to}")
            return True
    return False

if __name__ == '__main__':
    numbers = get_input()
    for index in range(preample,len(numbers)):
        if not check_XMAS_valid(index, numbers):
            print(f"{numbers[index]} is not adding up!!")
            break
