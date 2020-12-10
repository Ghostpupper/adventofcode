import copy
import re
from input_getter import get_input
pointer = 0
accu = 0
op_no = 1
old_pointers = []

regex = r"(nop|acc|jmp) (.)(.*)$"

def no_op(neg=False, num= 0):
    global pointer, op_no
    # print(f"{pointer}: nop {'-' if neg else '+'} {num} | {op_no}")
    pointer += 1

def jump(neg: bool, num: int):
    global pointer, old_pointers, op_no
    # print(f"{pointer}: jmp {'-' if neg else '+'} {num} | {op_no}")
    if neg:
        pointer -= num
    else:
        pointer += num

def acc(neg: bool, num: int):
    global accu, pointer, op_no
    # print(f"{pointer}: acc {'-' if neg else '+'} {num} | {op_no}")
    if neg:
        accu -= num
    else:
        accu += num
    pointer += 1


operation_map = {
    "nop": no_op,
    "acc": acc,
    "jmp": jump
}

def make_op(operation: str, neg: bool, num: int):
    operation_map[operation](neg, num)

def reset_counters():
    global accu, pointer, op_no, old_pointers
    accu = 0
    pointer = 0
    op_no = 1
    old_pointers = []

def check_if_it_finishes(test_list):
    global accu, pointer, op_no, old_pointers
    reset_counters()
    while pointer not in old_pointers:
        if pointer >= len(test_list):
            print("It finishes!")
            return True
        operation = test_list[pointer]
        old_pointers.append(pointer)
        make_op(operation=operation[0], neg=operation[1], num=operation[2])
        op_no += 1
    else:
        print("Starts to loop...")
        return False

if __name__ == '__main__':
    in_txt = get_input()
    parsed_list = []
    for i in in_txt:
        parsed = re.findall(regex, i)[0]
        parsed = [parsed[0], True if parsed[1] == '-' else False, int(parsed[2])]
        parsed_list.append(parsed)

    if check_if_it_finishes(parsed_list):
        print(f'accu is now {accu}')
    for i, entry in enumerate(parsed_list):
        if entry[0] == 'nop':
            entry[0] = 'jmp'
            print(f"Trying nop->jmp {entry[2]} at line {i+1}")
            if check_if_it_finishes(parsed_list):
                print(f'accu is now {accu}')
                break
            entry[0] = 'nop'
        elif entry[0] == 'jmp':
            entry[0] = 'nop'
            print(f"Trying jmp->nop {entry[2]} at line {i+1}")
            if check_if_it_finishes(parsed_list):
                print(f'accu is now {accu}')
                break
            entry[0] = 'jmp'
        else:
            continue



