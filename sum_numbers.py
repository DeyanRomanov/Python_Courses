number = int(input())
income_number = int(input())
counters = 0
counters += income_number
while counters < number:
    income_number = int(input())
    counters += income_number

print(counters)
