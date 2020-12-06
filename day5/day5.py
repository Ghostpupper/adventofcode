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
    seat_id_list = []
    for ticket in ticket_list:
        row_code = ticket[:7]
        column_code = ticket[7:]
        column_code = column_code.replace('\n', '')

        row = get_row(row_code)
        col = get_column(column_code)

        seat_id = row * 8 + col
        print(seat_id)
        for id in seat_id_list:
            if seat_id < id:
                break
        else:
            cur_highest_id = seat_id
        seat_id_list.append(seat_id)

    print(cur_highest_id)



