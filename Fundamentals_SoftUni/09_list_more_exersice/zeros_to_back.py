numbers = input().split(', ')

zero_counter = 0
new_list = []
for number in numbers:
    if int(number) == 0:
        zero_counter += 1
    else:
        new_list.append(int(number))
for zeros in range(zero_counter):
    new_list.append(0)

print(new_list)
