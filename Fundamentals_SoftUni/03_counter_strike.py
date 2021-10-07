initial_energy = int(input())
distance = input()
games_counter = 0
wins = 0

while not distance == 'End of battle':
    distance = int(distance)
    if distance <= initial_energy:
        initial_energy -= distance
        wins += 1
        games_counter += 1
        if wins % 3 == 0:
            initial_energy += games_counter
            wins = 0
    else:
        print(f"Not enough energy! Game ends with {games_counter} won battles and {initial_energy} energy")
        break
    distance = input()

else:
    print(f"Won battles: {games_counter}. Energy left: {initial_energy}")
