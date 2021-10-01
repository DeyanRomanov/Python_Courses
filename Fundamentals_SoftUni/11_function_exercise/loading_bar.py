def loading_bar(number):
    print(f'{number}%', end=' ')
    number //= 10
    if number < 10:
        print(f"[{'%' * number}{'.' * (10 - number)}]")
        print('Still loading...')
    else:
        print('Complete!')
        print(f"[{'%' * number}{'.' * (10 - number)}]")


loading_number = int(input())

loading_bar(loading_number)
