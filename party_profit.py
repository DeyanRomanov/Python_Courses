party_size = int(input())
days_of_adventure = int(input())

earning_money = 0

for day in range(1, days_of_adventure + 1):
    earning_money += 50
    if day % 10 == 0:
        party_size -= 2
    if day % 15 == 0:
        party_size += 5
    earning_money -= party_size * 2
    if day % 3 == 0:
        earning_money -= party_size * 3
        if day % 5 == 0:
            earning_money -= party_size * 2
    if day % 5 == 0:
        earning_money += party_size * 20
print(f'{party_size} companions received {int(earning_money / party_size)} coins each.')
