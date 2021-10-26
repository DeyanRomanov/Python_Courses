numbers_of_elements = int(input())

total_elements = set()
for _ in range(numbers_of_elements):
    elements_list = set(input().split())
    total_elements = total_elements.union(elements_list)

[print(x) for x in total_elements]
