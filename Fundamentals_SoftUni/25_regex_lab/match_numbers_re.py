import re

text = input()
pattern = r"(^|(?<=\s))-?\d*\.?\d*($|(?=\s))"

numbers = re.finditer(pattern, text)

for num in numbers:
    print(f'{num.group()}', end=' ')
