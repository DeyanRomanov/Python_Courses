import re

inputs = int(input())
for n in range(inputs):
    counter = 0
    text = input()
    pattern = r"(?P<sep>\|)(?P<name>[A-Z]{4,})(?P=sep):#(?P<title>[A-Za-z]+\s[A-Za-z]+)#"

    for match in re.finditer(pattern, text):
        counter += 1
        print(f"{match.group('name')}, The {match.group('title')}")
        print(f">> Strength: {len(match.group('name'))}")
        print(f">> Armour: {len(match.group('title'))}")
    if counter == 0:
        print('Access denied!')
