prepare = int(input())
prepare *= 750
dishes = input()
counter = 0
pot = 0
plate = 0
total_preparation = 0
while dishes != 'End':
    dishes = int(dishes)
    counter += 1
    if counter < 3:
        need_preparation = dishes * 5
        plate += dishes
    else:
        need_preparation = dishes * 15
        pot += dishes
        counter = 0
    total_preparation += need_preparation
    if prepare >= total_preparation:
        dishes = input()
    else:
        print(f"Not enough detergent, {total_preparation - prepare} ml. more necessary!")
        break
if prepare >= total_preparation:
    print(
    f"Detergent was enough!\n{plate} dishes and {pot} pots were washed.\nLeftover detergent {abs(total_preparation - prepare)} ml.")
