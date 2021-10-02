
# •	"add {people}" – you should add the number of people in the last wagon
# •	"insert {index} {people}" - you should add the number of people at the given wagon
# •	"leave {index} {people}" - you should remove the number of people from the wagon

number_of_trains = int(input())
trains = [int(0) for _ in range(number_of_trains)]

command = input().split()

while not command[0] == 'End':
    number_of_people = int(command[-1])
    index = int(command[1])
    command_name = command[0]
    if command_name == 'add':
        trains[-1] += number_of_people
    elif command_name == 'insert':
        trains[index] += number_of_people
    elif command_name == 'leave':
        trains[index] -= number_of_people
    command = input().split()

print(trains)