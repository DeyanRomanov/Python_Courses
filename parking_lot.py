number_of_cars = int(input())

cars_in_parking = set()

for car in range(number_of_cars):
    command, plates = input().split(', ')
    if command == 'IN':
        cars_in_parking.add(plates)
    else:
        cars_in_parking.remove(plates)

if cars_in_parking:
    for car in cars_in_parking:
        print(car)

else:
    print("Parking Lot is Empty")
