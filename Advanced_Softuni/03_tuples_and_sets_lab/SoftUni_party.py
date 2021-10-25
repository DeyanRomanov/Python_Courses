number_of_reservations = int(input())

reservations = set()
people_who_not_come = set()
for people in range(number_of_reservations):
    reservations.add(input())

names = input()

while not names == 'END':
    people_who_not_come.add(names)
    names = input()

total_guests = reservations - people_who_not_come
vip = []
regular = []
print(len(total_guests))
for guest in total_guests:
    if guest[0].isdigit():
        vip.append(guest)
    else:
        regular.append(guest)
for vips in sorted(vip):
    print(vips)
for normal in sorted(regular):
    print(normal)
