def sets(start, end):
    set_nums = set()
    for num in range(start, end + 1):
        set_nums.add(num)
    return set_nums


intersections = int(input())

first_set = set()
second_set = set()
longest_set = set()

for _ in range(intersections):
    first_range, second_range = input().split('-')

    start_first, end_first = first_range.split(',')
    start_second, end_second = second_range.split(',')
    first_set = sets(int(start_first), int(end_first))
    second_set = sets(int(start_second), int(end_second))

    first_set.intersection_update(second_set)
    if len(first_set) > len(longest_set):
        longest_set = first_set

longest_set_as_list = sorted(list(longest_set))

print(f"Longest intersection is {longest_set_as_list} with length {len(longest_set)}")
