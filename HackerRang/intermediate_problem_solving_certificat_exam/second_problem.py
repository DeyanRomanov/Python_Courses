numbers_of_elements, number_of_rows = map(int, input().split())
my_lists = [0] * numbers_of_elements
for _ in range(number_of_rows):
    start_index, end_index, number = map(int, input().split())
    for x in range(start_index - 1, end_index):
        my_lists[x] += number

print(max(my_lists))