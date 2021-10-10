def registers(park_dict, names, plates):
    if names not in park_dict:
        park_dict[names] = plates
        print(f"{names} registered {plates} successfully")
    else:
        print(f"ERROR: already registered with plate number {plates}")
    return park_dict


def unregisters(park_dict, names):
    if names not in park_dict:
        print(f"ERROR: user {names} not found")
    else:
        print(f"{names} unregistered successfully")
        park_dict.pop(names)
    return park_dict


number_of_people = int(input())

parking_dict = {}

for people in range(number_of_people):
    car = input().split()
    if len(car) > 2:
        registered, name, plate = car[0], car[1], car[2]
    else:
        registered, name = car[0], car[1]
    if registered == 'register':
        parking_dict = registers(parking_dict, name, plate)
    elif registered == 'unregister':
        parking_dict = unregisters(parking_dict, name)

for key, value in parking_dict.items():
    print(f'{key} => {value}')
