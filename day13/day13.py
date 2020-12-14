from input_getter import get_input

def parse_bus_schedule(ugly_version: str):
    ugly_list = ugly_version.split(',')
    not_so_ugly_list = []
    for entry in ugly_list:
        if entry.isnumeric():
            not_so_ugly_list.append(int(entry))
    not_so_ugly_list.sort()
    return not_so_ugly_list


if __name__ == '__main__':
    in_txt = get_input()
    arrival = int(in_txt[0])
    bus_schedule = parse_bus_schedule(in_txt[1])
    print(bus_schedule)
    print(arrival)
    closest_time = 0
    id_times_dif = 0
    for index, bus_time in enumerate(bus_schedule):
        acc_bus_time = bus_schedule[index]
        while acc_bus_time < arrival:
            acc_bus_time += bus_time

        print(f"{bus_time} : {acc_bus_time}")
        if acc_bus_time < closest_time or not closest_time:
            closest_time = acc_bus_time
            id_times_dif = (closest_time - arrival)*bus_time
    print(f"{closest_time} -> {id_times_dif}")

