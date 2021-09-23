command = input()

coffee_counter = 0
coffee_list = ['coding', 'movie', 'dog', 'cat', 'CODING', 'MOVIE', 'DOG', 'CAT']
while not command == 'END':
    if command in coffee_list:
        coffee_counter += 1
        if command.isupper():
            coffee_counter += 1
    if coffee_counter > 5:
        print(f'You need extra sleep')
        break
    command = input()
else:
    print(coffee_counter)
