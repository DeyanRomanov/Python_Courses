# Write a program which reads four integer numbers. It should add the first
# to the second number, integer divide the sum by the third number and multiply
# the result by the fourth number. Print the final result.
first_number = int(input())
second_number = int(input())
tird_number = int(input())
fourth_number = int(input())

calculate = int((first_number + second_number) / tird_number) * fourth_number

print(int(calculate))