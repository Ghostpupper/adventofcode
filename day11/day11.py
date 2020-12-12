from collections import Counter
from copy import copy

from input_getter import get_input

seats_matrix = []
l_seats_o = []
count = 0

class Position:
    def __init__(self, x, y, occupied):
        self.x = x
        self.y = y
        self.status = occupied
        self.adjacent_seats = []
        self.find_adjacent_seats()

    def make_vacant(self):
        lst_cpy = list(seats_matrix[self.y])
        lst_cpy[self.x] = 'L'
        seats_matrix[self.y] = ''.join(lst_cpy)
        self.status = 'L'

    def make_occupied(self):
        lst_cpy = list(seats_matrix[self.y])
        lst_cpy[self.x] = '#'
        seats_matrix[self.y] = ''.join(lst_cpy)
        self.status = '#'

    def find_adjacent_seats(self):
        seats = []
        for y in range(-1, 2):
            for x in range(-1, 2):
                if not x and not y:
                    continue
                try:
                    pos_y = self.y + y
                    pos_x = self.x + x
                    if pos_x >= 0 and pos_y >= 0:
                        other_seat = seats_matrix[self.y+y][self.x+x]
                        if other_seat in ['#', 'L']:
                            seats.append(other_seat)
                except IndexError:
                    continue
        self.adjacent_seats = seats

    def apply_rule(self):
        cnt = Counter(self.adjacent_seats)
        if self.status == '#':
            if cnt['#'] >= 4:
                self.make_vacant()
        if self.status == 'L':
            if cnt['#'] == 0:
                self.make_occupied()

def make_seats_occupied_for_some_reason(text):
    return [line.replace('L', '#') for line in text]

def make_seat_objects():
    global seats_matrix, l_seats_o
    for y, line in enumerate(seats_matrix):
        for x, seat in enumerate(line):
            if not seat == '.':
                new_seat = Position(x, y, seat)
                l_seats_o.append(new_seat)

def apply_rule_on_all_seats():
    for seat_o in l_seats_o:
        seat_o.apply_rule()
    for seat_o in l_seats_o:
        seat_o.find_adjacent_seats()

def display_seats():
    global count
    count += 1
    print(f'-----------------{count}-----------------')
    for row in seats_matrix:
        if row.endswith('\n'):
            print(row, end='')
        else:
            print(row)

def count_occupied():
    cnt = 0
    for row in seats_matrix:
        cnt += Counter(row)['#']
    return cnt

if __name__ == '__main__':
    in_txt = make_seats_occupied_for_some_reason(get_input())
    seats_matrix = in_txt
    old_seating = []
    make_seat_objects()
    while not old_seating == seats_matrix:
        old_seating = copy(seats_matrix)
        apply_rule_on_all_seats()
        display_seats()

    print(f'Number of occupied seats are now: {count_occupied()}')

