from copy import copy

from adventofcode.input_getter import get_input

list_of_trajectories = [
    {'Right': 1, 'Down': 1},
    {'Right': 3, 'Down': 1},
    {'Right': 5, 'Down': 1},
    {'Right': 7, 'Down': 1},
    {'Right': 1, 'Down': 2},
]

class Traveler:
    def __init__(self, map: list, width: int, max_lines: int, trajectory=None):
        if trajectory is None:
            trajectory = {'Right': 3, 'Down': 1}
        self.cur_x_pos = 0
        self.cur_line = 0
        self.width = width
        self.max_lines = max_lines
        self.map = map
        self.out = False
        self.no_of_trees = 0
        self.right = trajectory['Right']
        self.down = trajectory['Down']

    def go(self) -> float:
        while not self.out:
            self.move()
        return float(self.no_of_trees)

    def show_info(self):
        print(f'Width is {self.width}')
        print(f'len is {self.max_lines}')

    def show_map(self):
        for i in range(self.max_lines):
            print(self.map[i])

    def show_cur_line(self):
        print(self.map[self.cur_line])

    def move(self):
        self.cur_line += self.down
        self.cur_x_pos += self.right
        self.check_tree()

    def check_tree(self):
        try:
            string_copy: str = copy(self.map[self.cur_line])
        except IndexError:
            self.out = True
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
    map = get_input()
    ex_line: str = map[0]
    width = ex_line.find('\n')
    max_lines = len(map)
    list_of_res = []
    for traj in list_of_trajectories:
        traveler = Traveler(width=width, max_lines=max_lines, map=copy(map), trajectory=traj)
        print(f"- Right {traj['Right']}, down {traj['Down']}")
        trees_hit = traveler.go()
        print(f"trees hit: {trees_hit}")
        list_of_res.append(trees_hit)

    print(f"{list_of_res} multiplied together:")
    crazy_num: float = list_of_res[0]
    for num in list_of_res[1:]:
        crazy_num *= num
    print(crazy_num)

