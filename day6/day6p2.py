from input_getter import get_input

if __name__ == '__main__':
    in_txt = get_input()
    in_cpy = []
    print(in_txt)
    j = ''
    for i in in_txt:
        if i == '\n':
            i = i.replace('\n', '')
        if '\n' in i:
            i = i.replace('\n', '|')

        j += i
        if not i:
            in_cpy.append(j.rstrip('|'))
            j = ''
    else:
        in_cpy.append(j.rstrip('|'))
    print(in_cpy)
    answers = 0
    for group in in_cpy:
        person = group.split('|')
        print(person)
        first_ans = person.pop()
        if person:
            other_ans = person
            for an in first_ans:
                for other_an in other_ans:
                    if an not in other_an:
                        break
                else:
                    answers += 1
        else:
            answers += len(first_ans)

    print(answers)

