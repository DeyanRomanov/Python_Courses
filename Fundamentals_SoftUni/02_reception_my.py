first_worker = int(input())
second_worker = int(input())
third_worker = int(input())
students = int(input())

students_per_hour = first_worker + second_worker + third_worker
hours_counter = 0

while students > 0:
    hours_counter += 1
    if hours_counter % 4 == 0:
        hours_counter += 1
    students -= students_per_hour

print(f'Time needed: {hours_counter}h.')
