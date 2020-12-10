import re
from input_getter import get_input
pointer = 0
accu = 0
op_no = 1
old_pointers = []

regex = r"(nop|acc|jmp) (.)(.*)$"

def no_op(neg=False, num= 0):
    global pointer, op_no
    print(f"{pointer}: nop {'-' if neg else '+'} {num} | {op_no}")
    pointer += 1

def jump(neg: bool, num: int):
    global pointer, old_pointers, op_no
    print(f"{pointer}: jmp {'-' if neg else '+'} {num} | {op_no}")
    if neg:
        pointer -= num
    else:
        pointer += num

def acc(neg: bool, num: int):
    global accu, pointer, op_no
    print(f"{pointer}: acc {'-' if neg else '+'} {num} | {op_no}")
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


if __name__ == '__main__':
    in_txt = get_input()
    parsed_list = []
    for i in in_txt:
        parsed = re.findall(regex, i)[0]
        parsed = [parsed[0], True if parsed[1] == '-' else False, int(parsed[2])]
        parsed_list.append(parsed)

    while pointer not in old_pointers:
        operation = parsed_list[pointer]
        old_pointers.append(pointer)
        make_op(operation=operation[0], neg=operation[1], num=operation[2])
        op_no += 1
    else:
        print(f"{op_no}(!)")
        print(accu)






