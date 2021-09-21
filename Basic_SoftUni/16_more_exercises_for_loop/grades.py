number_of_students = int(input())
grades_two = 0
grades_three = 0
grades_four = 0
grades_five = 0
total_grades = 0

for x in range(number_of_students):
    student_grades = float(input())
    total_grades += student_grades
    if 2 <= student_grades <= 2.99:
        grades_two += 1
    elif 3 <= student_grades <= 3.99:
        grades_three += 1
    elif 4 <= student_grades <= 4.99:
        grades_four += 1
    elif 5 <= student_grades:
        grades_five += 1

percent_two = grades_two / number_of_students * 100
percent_three = grades_three / number_of_students * 100
percent_four = grades_four / number_of_students * 100
percent_five = grades_five / number_of_students * 100
average = total_grades / number_of_students

print(f'Top students: {percent_five:.2f}%')
print(f'Between 4.00 and 4.99: {percent_four:.2f}%')
print(f'Between 3.00 and 3.99: {percent_three:.2f}%')
print(f'Fail: {percent_two:.2f}%')
print(f'Average: {average:.2f}')
