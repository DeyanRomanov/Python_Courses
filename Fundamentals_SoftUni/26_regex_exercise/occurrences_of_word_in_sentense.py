import re

sentense = input().upper()
word = input().upper()

pattern = fr"(\b{word}\b)"

result = re.findall(pattern, sentense)
print(len(result))

