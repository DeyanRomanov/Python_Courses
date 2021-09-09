type_petrol = str(input()).lower()
litters = int(input())

if type_petrol == 'diesel' or type_petrol == 'gasoline' or type_petrol == 'gas':
    if litters >= 25:
        print(f'You have enough {type_petrol}.')
    else:
        print(f'Fill your tank with {type_petrol}!')
else:
    print(f'Invalid fuel!')
