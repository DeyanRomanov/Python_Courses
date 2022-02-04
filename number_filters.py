numbers = int(input())

even = []
odd = []
negative = []
positive = []


for num in range(numbers):
    number = int(input())
    if number % 2 == 0 or number == 0:
        even.append(number)
    else:
        odd.append(number)
    if number < 0:
        negative.append(number)
    else:
        positive.append(number)

command = input()

if command == 'even':
    print(even)
elif command == 'odd':
    print(odd)
elif command == 'negative':
    print(negative)
else:
    print(positive)
