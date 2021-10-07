import math

students = int(input())
lectures = int(input())
additional_bonus = int(input())

max_bonuses = 0
total_points = 0

for _ in range(students):
    point = int(input())
    bonus = point / lectures * (5 + additional_bonus)
    if max_bonuses < bonus:
        max_bonuses = bonus
        total_points = point

print(f"Max Bonus: {math.ceil(max_bonuses)}.")
print(f'The student has attended {total_points} lectures.')
