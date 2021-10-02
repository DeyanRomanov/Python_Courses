rooms = int(input())

total_chairs = 0
total_people = 0
is_free = True

for room in range(1, rooms + 1):
    chairs_and_people = input().split()
    chairs, people = chairs_and_people[0], int(chairs_and_people[1])
    if len(chairs) < people:
        print(f"{people - len(chairs)} more chairs needed in room {room}")
        is_free = False
    else:
        total_chairs += len(chairs)
        total_people += people

if is_free:
    print(f'Game On, {total_chairs - total_people} free chairs left')
