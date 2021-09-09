student_name = input()
grade = 0
common_evaluation = 0
inseminate = 0
while grade < 12:
    evaluation = float(input())
    if evaluation < 4:
        inseminate += 1
    else:
        common_evaluation += evaluation
    if inseminate > 1:
        print(f'{student_name} has been excluded at {grade} grade')
        break
    grade += 1
if grade >= 12:
    print(f"{student_name} graduated. Average grade: {common_evaluation / 12:.2f}")
