from copy import copy

from adventofcode.input_getter import get_input


class Traveler:
    def __init__(self, map: list, width: int, max_lines: int):
        self.cur_x_pos = 0
        self.cur_line = 0
        self.width = width
        self.max_lines = max_lines
        self.map = map
        self.out = False
        self.no_of_trees = 0

    def show_info(self):
        print(f'Width is {self.width}')
        print(f'len is {self.max_lines}')

    def show_map(self):
        for i in range(self.max_lines):
            print(self.map[i])

    def show_cur_line(self):
        print(self.map[self.cur_line])

    def move(self):
        self.cur_line += 1
        self.cur_x_pos += 3
        self.check_tree()

    def check_tree(self):
        try:
            string_copy: str = copy(self.map[self.cur_line])
        except IndexError:
            self.out = True
            self.show_map()
            print(f"number of trees hit: {self.no_of_trees}")
            return
        position = self.cur_x_pos % self.width
        check_pos = string_copy[position]
        if check_pos == '#':
            string_copy = string_copy[:position] + 'X' + string_copy[position+1:]
            self.map[self.cur_line] = string_copy
            self.no_of_trees += 1
        elif check_pos == '.':
            string_copy = string_copy[:position] + 'O' + string_copy[position + 1:]
            self.map[self.cur_line] = string_copy


if __name__ == '__main__':
    in_txt = get_input()
    ex_line: str = in_txt[0]
    dude = Traveler(width=ex_line.find('\n'), max_lines=len(in_txt), map=in_txt)
    # dude.show_map()
    while not dude.out:
        dude.move()
