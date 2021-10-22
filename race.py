names_list = input().split(', ')
names_income = input()
names_dict = {}

for name in names_list:
    if name not in names_dict:
        names_dict[name] = []

while not names_income == 'end of race':
    name = ''
    km = 0
    for letter in names_income:
        if letter.isalpha():
            name += letter
        elif letter.isnumeric():
            km += int(letter)
    if name in names_dict:
        names_dict[name].append(km)
    names_income = input()

for name in names_dict:
    names_dict[name] = sum(names_dict[name])

counter = 0
for name, km in sorted(names_dict.items(), key=lambda x: -x[1]):
    counter += 1
    if counter == 1:
        print(f'1st place: {name}')
    elif counter == 2:
        print(f'2nd place: {name}')
    elif counter == 3:
        print(f"3rd place: {name}")
        break
