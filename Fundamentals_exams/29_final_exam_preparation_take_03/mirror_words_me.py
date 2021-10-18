import re

text = input()
mirrors_list = []

pattern = r"(?P<sep>(@|#))(?P<word>[A-Za-z]{3,})(?P=sep){2}(?P<mirr_word>[A-Za-z]{3,})(?P=sep)"

result = re.finditer(pattern, text)
match_counter = 0

for mirror in result:
    match_counter += 1
    a = mirror.group('word')
    b = mirror.group('mirr_word')
    if a == b[::-1]:
        mirrors_list.append(f"{a} <=> {b}")

if len(mirrors_list) > 0:
    print(f"{match_counter} word pairs found!")
    print(f'The mirror words are:')
    print(", ".join(mirrors_list))
else:
    if match_counter > 0:
        print(f"{match_counter} word pairs found!")
    else:
        print("No word pairs found!")
    print("No mirror words!")
