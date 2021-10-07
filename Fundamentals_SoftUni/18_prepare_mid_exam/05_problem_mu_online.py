def healer(values, healthy):
    if healthy + values > 100:
        values = 100 - healthy
        healthy = 100
    else:
        healthy += values
    print(f"You healed for {values} hp.\nCurrent health: {healthy} hp.")
    return healthy


def fight(commands, values, healthy, room):
    healthy -= values
    if healthy <= 0:
        print(f"You died! Killed by {commands}.\nBest room: {room}")
    else:
        print(f"You slayed {commands}.")
    return healthy


dungeons_rooms = input().split('|')
health = 100
bitcoin = 0
room_counter = 0
is_death = False

while len(dungeons_rooms) > 0:
    room_counter += 1
    rooms = dungeons_rooms[0].split()
    command = rooms[0]
    value = int(rooms[1])
    if command == 'potion':
        health = healer(value, health)
    elif command == 'chest':
        bitcoin += value
        print(f"You found {value} bitcoins.")
    else:
        health = fight(command, value, health, room_counter)
        if health <= 0:
            is_death = True
            break
    dungeons_rooms.pop(0)
if not is_death:
    print(f"You've made it!\nBitcoins: {bitcoin}\nHealth: {health}")
