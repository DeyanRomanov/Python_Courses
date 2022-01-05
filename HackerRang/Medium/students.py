number_of_students = int(input())

records = {}

for students in range(number_of_students):
    student = input()
    store = float(input())
    records[student] = store

lowest_grade = ''
counter = 0
for students, grades in sorted(records.items(), key=lambda x: (x[1], x[0])):
    if counter == 0:
        lowest_grade = grades
        del records[students]
    if counter > 0:
        if lowest_grade == grades:
            del records[students]
    counter += 1

first_grade = ''
second_grade = []
counter = 0
for students, grades in sorted(records.items(), key=lambda x: (x[1], x[0])):
    if counter == 0:
        first_grade = grades
        second_grade.append(students)
    if counter > 0:
        if first_grade == grades:
            second_grade.append(students)
    counter += 1

for names in second_grade:
    print(names)
