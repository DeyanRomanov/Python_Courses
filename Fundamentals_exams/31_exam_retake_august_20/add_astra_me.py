import re

text_string = input()
pattern = r"(?P<sep>[#|\|])(?P<product>[A-Za-z\s]+)(?P=sep)(?P<expire>(\d{1}|\d{2})/\d{2}/\d{2})(?P=sep)(?P<cal>\d+)(?P=sep)"

total_calories = 0
for match in re.finditer(pattern, text_string):
    total_calories += int(match.group('cal'))

total_calories //= 2000
print(f"You have food to last you for: {total_calories} days!")

for match in re.finditer(pattern, text_string):
    print(f"Item: {match.group('product')}, Best before: {match.group('expire')}, Nutrition: {match.group('cal')}")
