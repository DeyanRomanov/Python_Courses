number_ot_twice = int(input())
sum_of_numbers = 0
last_sum_of_numbers = 0
last_total = 0
total = 0
counter = 0

for x in range(number_ot_twice):
    number_one = int(input())
    number_two = int(input())
    sum_of_numbers = number_two + number_one
    if x != 0:
        if sum_of_numbers != last_sum_of_numbers:
            total = abs(sum_of_numbers - last_sum_of_numbers)
        if total > last_total:
            last_total = total
        if sum_of_numbers == last_sum_of_numbers:
            counter += 1
    last_sum_of_numbers = sum_of_numbers

if counter + 1 == number_ot_twice:
    print(f"Yes, value={last_sum_of_numbers}")
else:
    print(f"No, maxdiff={last_total}")
