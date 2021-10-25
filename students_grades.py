number_of_students = int(input())

students_and_grades_dict = {}
for names in range(number_of_students):
    student, grade = input().split()
    if student not in students_and_grades_dict:
        students_and_grades_dict[student] = []
    students_and_grades_dict[student].append(grade)

for names, grades in students_and_grades_dict.items():
    grades = [float(grade) for grade in grades]
    average_grades = sum(grades) / len(grades)
    grades_as_string = ' '.join(str(f"{x:.2f}") for x in grades)
    print(f"{names} -> {grades_as_string} (avg: {average_grades:.2f})")
