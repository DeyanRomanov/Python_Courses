number_of_list = int(input())
numbers = [int(x) for x in input().split()]
max_number = 100
my_list = [0] * max_number
for n in numbers:
    my_list[n] += 1
print(*my_list)
