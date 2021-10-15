import re

text = input()

while text:
    pattern = r"\d+"
    matches = re.finditer(pattern, text)
    for mach in matches:
        print(mach.group(), end=' ')
    text = input()
