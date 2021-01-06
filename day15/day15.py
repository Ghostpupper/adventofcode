starting_numbers = [1, 3, 2]

def add_number_to_list():
    global starting_numbers
    last_no = starting_numbers[-1]
    if last_no not in starting_numbers[:-1]:
        starting_numbers.append(0)
    else:
        last_index = find_latest_index(last_no)
        starting_numbers.append(last_index)

def find_latest_index(last_no: int, index=0):
    rev_list = reversed(starting_numbers[:-1])
    distance = 1
    for item in rev_list:
        if item == last_no:
            return distance
        distance += 1

def game(n):
    global starting_numbers
    while n >= len(starting_numbers):
        add_number_to_list()
    return starting_numbers[n]

def main():
    num = 2020
    print(game(num - 1))

if __name__ == '__main__':
    list_o_list = [[2,1,3], [1,2,3], [2,3,1], [3,2,1], [3,1,2], [1,20,11,6,12,0]]
    for o_list in list_o_list:
        starting_numbers = o_list
        main()

