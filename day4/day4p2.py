from adventofcode.input_getter import get_input
import re
"""
byr (Birth Year)
iyr (Issue Year)
eyr (Expiration Year)
hgt (Height)
hcl (Hair Color)
ecl (Eye Color)
pid (Passport ID)
cid (Country ID)
"""
req_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
ok_eyes = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']


def sort_out_passports(list_pp: list):
    tmp_pp: str = ""
    for line in list_pp:
        tmp_pp += line.replace('\n', ' ')
        if line == '\n' or line == list_pp[-1]:
            yield tmp_pp.replace('  ', '')
            tmp_pp = ""


def entry_spec_check(entry: str, value: str):
    if entry == 'byr':
        if not value.__len__() == 4:
            print(f"{value} is wrong")
            return False
        value = int(value)
        if value < 1920:
            print(f'{entry} {value} is too low')
            return False
        if value > 2002:
            print(f'{entry} {value} is too high')
            return False

    elif entry == 'iyr':
        if not value.__len__() == 4:
            print(f"{value} is wrong")
            return False
        value = int(value)
        if value < 2010:
            print(f'{entry} {value} is too low')
            return False
        if value > 2020:
            print(f'{entry} {value} is too high')
            return False

    elif entry == 'eyr':
        if not value.__len__() == 4:
            print(f"{value} is wrong")
            return False
        value = int(value)
        if value < 2020:
            print(f'{entry} {value} is too low')
            return False
        if value > 2030:
            print(f'{entry} {value} is too high')
            return False

    elif entry == 'hgt':
        if value.isnumeric():
            return False
        if not value[-2:] in ['cm', 'in']:
            return False
        l_value = int(value[:-2])
        if 'cm' in value:
            if l_value < 150 or l_value > 193:
                return False
        if 'in' in value:
            if l_value < 59 or l_value > 76:
                return False

    elif entry == 'hcl':
        if re.search(r"^#[a-f|0-9]{6}$", value):
            return True
        else:
            return False

    elif entry == 'ecl':
        if value not in ok_eyes:
            return False

    elif entry == 'pid':
        if not value.__len__() == 9:
            return False
    return True


def check_pp_validity(pp: str) -> bool:
    for field in req_fields:
        if field not in pp:
            print(f'{field} missing in pp')
            return False
    entry_list = pp.split(' ')
    for entry in entry_list:
        entry, value = entry.split(':')
        if not entry_spec_check(entry, value):
            print(f"{entry} is not correct")
            return False
    return True


if __name__ == '__main__':
    in_txt = get_input()
    sorted_pp: list = []
    valid_pp_count = 0
    for generated_pp in sort_out_passports(in_txt):
        sorted_pp.append(generated_pp)
    for pp in sorted_pp:
        print(pp)
        if check_pp_validity(pp):
            print('valid!')
            valid_pp_count += 1
    print(f'Total valid passports: {valid_pp_count}/{len(sorted_pp)}')
