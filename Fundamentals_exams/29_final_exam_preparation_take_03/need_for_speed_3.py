number_of_cars = int(input())


cars_dict = {}

for cars in range(number_of_cars):
    car = input()
    model, mileage, fuel = car.split('|')
    mileage = int(mileage)
    fuel = int(fuel)
    cars_dict[model] = [mileage, fuel]

commands = input()

while not commands == 'Stop':
    commands = commands.split(' : ')
    command = commands[0]
    if command == 'Drive':
        car, distance, fuel = commands[1], int(commands[2]), int(commands[3])
        if cars_dict[car][1] < fuel:
            print("Not enough fuel to make that ride")
        else:
            cars_dict[car][0] += distance
            cars_dict[car][1] -= fuel
            print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
        if cars_dict[car][0] >= 100000:
            print(f"Time to sell the {car}!")
            cars_dict.pop(car)
    elif command == 'Refuel':
        car, fuel = commands[1], int(commands[2])
        if cars_dict[car][1] + fuel > 75:
            fuel = 75 - cars_dict[car][1]
            cars_dict[car][1] = 75
        else:
            cars_dict[car][1] += fuel
        print(f"{car} refueled with {fuel} liters")
    elif command == 'Revert':
        car, kilometers = commands[1], int(commands[2])
        cars_dict[car][0] -= kilometers
        if cars_dict[car][0] < 10000:
            cars_dict[car][0] = 10000
        else:
            print(f"{car} mileage decreased by {kilometers} kilometers")
    commands = input()

for key, value in sorted(cars_dict.items(), key=lambda x: (-x[1][0], x[0])):
    print(f"{key} -> Mileage: {value[0]} kms, Fuel in the tank: {value[1]} lt.")
