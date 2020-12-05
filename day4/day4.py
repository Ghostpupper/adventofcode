from adventofcode.input_getter import get_input
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


def sort_out_passports(list_pp: list):
    tmp_pp: str = ""
    for line in list_pp:
        tmp_pp += line.replace('\n', ' ')
        if line == '\n' or line == list_pp:
            yield tmp_pp
            tmp_pp = ""


def check_pp_validity(pp: str) -> bool:
    for field in req_fields:
        if field not in pp:
            print(f'{field} missing in pp')
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
