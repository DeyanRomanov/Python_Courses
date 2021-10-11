contest = input()

courses = {}
while not contest == 'no more time':
    username, course, point = contest.split(' -> ')
    point = int(point)
    if course not in courses:
        courses[course] = {username: point}
    else:
        if username not in courses[course]:
            courses[course].update({username: point})
        else:
            if courses[course][username] < point:
                courses[course][username] = point
    contest = input()

for key, value in courses.items():
    counter = 0
    print(f'{key}: {len(value)} participants')
    for k, v in sorted(courses[key].items(), key=lambda x: (-x[1], x[0])):
        counter += 1
        print(f'{counter}. {k} <::> {v}')

print(f'Individual standings:')

final_dict = {}
for value in courses.values():
    for k, v in value.items():
        if k not in final_dict:
            final_dict[k] = v
        else:
            final_dict[k] += v
counter = 0
for key, value in sorted(final_dict.items(), key=lambda x: (-x[1], x[0])):
    counter += 1
    print(f'{counter}. {key} -> {value}')


