import re

places = input()
pattern = r"(?P<sep>[/|=])(?P<word>[A-Z]{1}[A-Za-z]{2,})(?P=sep)"
destinations = re.finditer(pattern, places)
destinations_list = []

for destination in destinations:
    destinations_list.append(destination.group('word'))

print(f'Destinations: {", ".join(destinations_list)}')
points = 0
for destination in destinations_list:
    points += len(destination)
print(f'Travel Points: {points}')
