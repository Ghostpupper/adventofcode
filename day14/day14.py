import re

from input_getter import get_input

x_mask = ''
mask = int('0', 2)
mask_mask = int('0', 2)
memory_stack = {}

total = 0

def change_mask(new_mask: str):
    global mask, mask_mask, x_mask
    mask = int(new_mask.replace('X', '0').lstrip('0'), 2)
    mask_mask = int(new_mask.replace('1', '0').replace('X', '1'), 2)
    x_mask = new_mask
    return mask

def update_mem(address: int, value: str):
    global mask, memory_stack
    bin_val = int(value)
    res = (bin_val & mask_mask) | mask
    memory_stack[address] = res
    print(f"[{address}] {res} (decimal {int(res)})")

if __name__ == '__main__':
    in_txt = get_input()

    for line in in_txt:
        if 'mask' in line:
            change_mask(line.replace('mask = ', ''))
        if 'mem' in line:
            find = re.findall(r"mem\[(\d*)\] = (\d*)$", line)[0]
            adr = int(find[0])
            val = find[1]
            update_mem(adr, val)

    for mem in memory_stack.values():
        total += int(mem)

    print(total)



