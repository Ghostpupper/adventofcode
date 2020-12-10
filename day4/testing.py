import re

str = "3 faded blue bags, 4 dotted black bags"
pattern = r"((\d*) (\w* \w*) bags)"
while re.search(pattern, str):
    match = re.findall(pattern, str)[0]
    full_str = match[0]
    no = int(match[1])
    color = match[2]
    str = str.lstrip(full_str)

