from input_getter import get_input

class Boat:
    def __init__(self):
        self._dir_pointer = 0
        self._dir_list = ['E', 'S', 'W', 'N']
        self._facing = self._dir_list[self._dir_pointer]
        self._dir_dist = {
            'N': 0,
            'S': 0,
            'E': 0,
            'W': 0
        }
        self.manhattan = self.manhattan_distance()

    def move(self, letter, number: int):
        """
        :param letter:
        :param number:
        :return:
        """
        if letter == 'F':
            self._dir_dist[self._facing] += number
            print(f'{self._dir_dist}')
        if letter == 'R':
            steps = number / 90
            self._dir_pointer = int((self._dir_pointer + steps) % 4)
            self._facing = self._dir_list[self._dir_pointer]
            print(f'Facing {self._facing}')
        if letter == 'L':
            steps = number / 90
            p = int((self._dir_pointer - steps) % 4)
            self._dir_pointer = p
            self._facing = self._dir_list[int(self._dir_pointer)]
            print(f'Facing {self._facing}')
        if letter in self._dir_list:
            self._dir_dist[letter] += number
            print(f'{self._dir_dist}')

    def manhattan_distance(self):
        vertical = abs(self._dir_dist['N'] - self._dir_dist['S'])
        horizontal = abs(self._dir_dist['W'] - self._dir_dist['E'])
        self.manhattan = man = vertical + horizontal
        return man

if __name__ == '__main__':
    in_txt = get_input()
    boat = Boat()
    for inst in in_txt:
        letter = inst[0]
        num = int(inst[1:])
        boat.move(letter, num)
    print(boat.manhattan_distance())

