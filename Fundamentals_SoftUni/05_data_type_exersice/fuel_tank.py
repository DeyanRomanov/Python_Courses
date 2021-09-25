number_of_pours = int(input())

tank_capacity = 255
littre_in = 0
for pour in range(number_of_pours):
    pour_per_time = int(input())
    if pour_per_time > tank_capacity:
        print('Insufficient capacity!')
    else:
        tank_capacity -= pour_per_time
        littre_in += pour_per_time
print(littre_in)

