import re

sentese = input()
pattern = r"^|(?<=\b_{1})([A-Z]|[a-z]|\d)*(?=\s|$)"
result = []
matches = re.finditer(pattern, sentese)
for match in matches:
    result.append(match.group())
result = [res for res in result if len(res) > 0]
print(','.join(result).strip())
