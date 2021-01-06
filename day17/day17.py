import re

from input_getter import get_input

a_and_b = r"(\d{1,}) ([+*]) (\d{1,})"
find_paranth = r"\(([^\)\(]*)\)"

def calc_str(whole_string: str):
    paranthes = re.findall(find_paranth, whole_string)
    if paranthes:
        res = calc_no_panths(paranthes[0])
        new_str = whole_string.replace(f"({paranthes[0]})", res)
        return calc_str(new_str)
    return calc_no_panths(whole_string)

def calc_no_panths(calcul_string):
    calc_pairs = re.findall(a_and_b, calcul_string)
    pair = calc_pairs[0]
    a = int(pair[0])
    b = int(pair[2])
    pair_str = f"{pair[0]} {pair[1]} {pair[2]}"
    c = a + b if pair[1] == '+' else a * b
    new_calcul_string = calcul_string.replace(pair_str, str(c))
    if '*' in new_calcul_string or '+' in new_calcul_string:
        return calc_no_panths(new_calcul_string)
    return new_calcul_string


if __name__ == '__main__':
    in_txt = get_input()
    all_res = 0
    ''.isnumeric()
    for text in in_txt:
        res = int(calc_str(text))
        all_res += res
        print(f"- [{text[:-1] if not text[-1].isnumeric() else text}] becomes: {res}.")
    print(all_res)

