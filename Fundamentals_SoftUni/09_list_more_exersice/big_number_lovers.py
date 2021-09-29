numbers = input().split()

numbers.sort()
new_list = []

for number in numbers:
    new_list.insert(0, number)

print(''.join(new_list))
