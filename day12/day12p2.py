from copy import copy

from input_getter import get_input

dir_list = ['E', 'S', 'W', 'N']

class Boat:
    def __init__(self):
        self._dir_pointer = 0
        # self._facing = self._dir_list[self._dir_pointer]
        self._dir_dist = {
            'E': 0,
            'S': 0,
            'W': 0,
            'N': 0
        }
        self.way_point = {
            'E': 10,
            'S': 0,
            'W': 0,
            'N': 1
        }
        self.manhattan = self.manhattan_distance()

    def move(self, letter, number: int):

        if letter == 'F':
            for d in dir_list:
                self._dir_dist[d] += number*self.way_point[d]
            print(f'{self._dir_dist}')
        if letter == 'R':
            steps = number / 90
            for i in range(int(steps)):
                tmp_way: dict = copy(self.way_point)
                keys = list(tmp_way.keys())
                self.way_point[keys[0]] = tmp_way[keys[3]]
                self.way_point[keys[1]] = tmp_way[keys[0]]
                self.way_point[keys[2]] = tmp_way[keys[1]]
                self.way_point[keys[3]] = tmp_way[keys[2]]
        if letter == 'L':
            steps = number / 90
            for i in range(int(steps)):
                tmp_way: dict = copy(self.way_point)
                keys = list(tmp_way.keys())
                self.way_point[keys[0]] = tmp_way[keys[1]]
                self.way_point[keys[1]] = tmp_way[keys[2]]
                self.way_point[keys[2]] = tmp_way[keys[3]]
                self.way_point[keys[3]] = tmp_way[keys[0]]
        if letter in dir_list:
            self.way_point[letter] += number
            print(f'{self.way_point}')

    def manhattan_distance(self):
        vertical = abs(self._dir_dist['N'] - self._dir_dist['S'])
        horizontal = abs(self._dir_dist['W'] - self._dir_dist['E'])
        self.manhattan = man = vertical + horizontal
        return man

if __name__ == '__main__':
    in_txt = get_input()
    boat = Boat()
    for inst in in_txt:
        print(inst, end='')
        letter = inst[0]
        num = int(inst[1:])
        boat.move(letter, num)
    print(boat.manhattan_distance())

