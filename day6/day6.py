from input_getter import get_input

if __name__ == '__main__':
    in_txt = get_input()
    in_cpy = []
    print(in_txt)
    j = ''
    for i in in_txt:
        if '\n' in i:
            i = i.replace('\n', '')

        j += i
        if not i:
            in_cpy.append(j)
            j = ''
    else:
        in_cpy.append(j)
    print(in_cpy)
    no_dup = []
    total = 0
    for group in in_cpy:
        a = (set(list(group)))
        total += len(a)
        no_dup.append(a)
    print(no_dup)
    print(total)
