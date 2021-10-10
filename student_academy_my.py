students = int(input())

academy_dict = {}

for student in range(students):
    name = input()
    grade = float(input())
    if name not in academy_dict:
        academy_dict[name] = []
    academy_dict[name].append(grade)

for key, value in academy_dict.items():
    academy_dict[key] = sum(value) / len(value)

academy_dict = {key: value for key, value in academy_dict.items() if value >= 4.50}
academy_dict = dict(sorted(academy_dict.items(), key=lambda x: x[1], reverse=True))
for key, value in academy_dict.items():
    print(f'{key} -> {academy_dict[key]:.2f}')
