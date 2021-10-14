import re

text = input()
pattern = r"\+359(?P<sep>[-\s])2(?P=sep)\d{3}(?P=sep)\d{4}"

result = re.finditer(pattern, text)
result = [re.group() for re in result]

print(', '.join(result))
