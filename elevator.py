people = int(input())
capacity = int(input())

courses = people // capacity
corses_2 = people % capacity
if corses_2 > 0:
    courses += 1
print(courses)
