from adventofcode.input_getter import get_input

row_bin_trs = {'F': '0', 'B': '1'}
col_bin_trs = {'R': '0', 'L': '1'}

def get_row(row_c: str) -> int:
    binary_version = row_c.replace('F', '0')
    binary_version = binary_version.replace('B', '1')
    binary_value = int(binary_version, 2)
    return binary_value

def get_column(row_c: str) -> int:
    binary_version = row_c.replace('L', '0')
    binary_version = binary_version.replace('R', '1')
    binary_value = int(binary_version, 2)
    return binary_value

if __name__ == '__main__':
    ticket_list = get_input()
    seats_matrix = [[0]*128]*8
    for i in seats_matrix:
        print(f"{i}\n")
    # for ticket in ticket_list:
    #     row_code = ticket[:7]
    #     column_code = ticket[7:]
    #     column_code = column_code.replace('\n', '')
    #
    #     row = get_row(row_code)
    #     col = get_column(column_code)
    #     try:
    #         seats_matrix[col][row] = 1
    #     except IndexError:
    #         print(f"row:{row} col:{col} is out of range")
    #         raise
    #     seat_id = row * 8 + col
    # empty_seats = []
    # for col in range(len(seats_matrix)):
    #     for row, value in enumerate(seats_matrix[col]):
    #         if row == 0 or row == 127:
    #             continue
    #         if not value:
    #             empty_seat = [col, row]
    #             empty_seats.append(empty_seat)
    #
    # print(empty_seats)



