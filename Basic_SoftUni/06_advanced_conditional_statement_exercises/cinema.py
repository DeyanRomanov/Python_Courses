film = input()
r = int(input())
c = int(input())
places = r * c
income = 0
if film == 'Premiere':
    income = places * 12
elif film == 'Normal':
    income = places * 7.50
elif film == 'Discount':
    income = places * 5.00
print(f'{income:.2f} leva')
