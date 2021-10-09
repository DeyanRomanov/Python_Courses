students = input()

students_dict = {}

while ':' in students:
    name, ids, course = students.split(':')
    if course not in students_dict:
        students_dict[course] = {}
    students_dict[course][ids] = name
    students = input()

students = students.replace('_', ' ')
for key, value in students_dict[students].items():
    print(f"{value} - {key}")
