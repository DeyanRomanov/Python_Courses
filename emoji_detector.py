import re


text = input()

cool = 1
for l in text:
    if l.isnumeric():
        cool *= int(l)

print(f"Cool threshold: {cool}")

pattern = r"(?P<sep>:{2}|\*{2})(?P<emojy>[A-Z]{1}[a-z]{2,})(?P=sep)"

result = re.finditer(pattern, text)

print(f"{len([*re.finditer(pattern, text)])} emojis found in the text. The cool ones are:")

for res in result:
    coolest = 0
    a = res.group('emojy')
    for l in a:
        coolest += ord(l)
    if coolest > cool:
        print(res.group())
