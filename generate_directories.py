import os
from pathlib import Path

list_dir = os.listdir('.')
cur_dir = Path(os.curdir)
for day in range(1, 25):
    day_dir = f'day{day}'
    if day_dir not in list_dir:
        print(f"making dir: {day_dir}")
        os.mkdir(day_dir)
    elif day_dir in list_dir:
        cur_fold_dir = os.listdir(day_dir)
        print(cur_fold_dir)
        if f'day{day}.py' not in cur_fold_dir:
            print(f"Creating {day_dir}/day{day}.py")
            with open(f"{day_dir}/day{day}.py", 'w') as new_file:
                new_file.writelines("from adventofcode.input_getter import get_input\n")
                new_file.writelines("\n")
                new_file.writelines("if __name__ == '__main__':\n")
                new_file.writelines("    in_txt = get_input()\n")
        if f'day{day}p2.py' not in cur_fold_dir:
            print(f"Creating {day_dir}/day{day}p2.py")
            with open(f"{day_dir}/day{day}p2.py", 'w') as new_file:
                new_file.writelines("from adventofcode.input_getter import get_input\n")
                new_file.writelines("\n")
                new_file.writelines("if __name__ == '__main__':\n")
                new_file.writelines("    in_txt = get_input()\n")
        if f'input.txt' not in cur_fold_dir:
            print(f"Creating {day_dir}/input.txt")
            with open(f"{day_dir}/input.txt", 'w') as new_file:
                new_file.write("empty!")