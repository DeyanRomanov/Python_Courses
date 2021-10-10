courses = input()

courses_and_students = {}

while not courses == 'end':
    course, student = courses.split(' : ')
    if course not in courses_and_students:
        courses_and_students[course] = []
    courses_and_students[course].append(student)
    courses = input()

courses_and_students = dict(sorted(courses_and_students.items(), reverse=True, key=lambda x: len(x[1])))
for key, value in courses_and_students.items():
    print(f'{key}: {len(value)}')
    for names in sorted(value):
        print(f'-- {names}')
