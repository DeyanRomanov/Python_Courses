# The input will be a single string containing the animals separated by comma and a single space ", "
animals = input()

list_whit_animals = animals.split(", ")
number_of_sheep = 0

if list_whit_animals[-1] == 'wolf':
    print(f'Please go away and stop eating my sheep')
for index, word in enumerate(list_whit_animals):
    if not index == len(list_whit_animals) - 1 and word == 'wolf':
        number_of_sheep = len(list_whit_animals) - 1 - index
        print(f'Oi! Sheep number {number_of_sheep}! You are about to be eaten by a wolf!')
