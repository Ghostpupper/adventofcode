from adventofcode.input_getter import get_input
import re

if __name__ == '__main__':
    password_list = get_input()
    ok_passwords = 0
    for line in password_list:
        match = re.findall(r'(\d*)-(\d*) (.): (.*)', line)[0]
        print(f"{line[:-1]}")
        lower = int(match[0])
        higher = int(match[1])
        letter = match[2]
        password = match[3]
        instances = 0
        for char in password:
            if char == letter:
                instances += 1
        print(f"instances of '{letter}' is {instances}")
        if instances < lower:
            print("too few")
            continue
        elif instances > higher:
            print("too many!")
            continue
        print("ok!")
        ok_passwords += 1

    print(f"total ok: {ok_passwords}")





