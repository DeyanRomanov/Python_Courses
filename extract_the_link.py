import re


text = input()
while text:
    pattern = r"www.[A-Za-z0-9]+[\-[A-Za-z0-9]*[A-Za-z0-9]+\.[a-z]+[\.a-z]*"

    result = re.finditer(pattern, text)
    for res in result:
        print(res.group())
    text = input()