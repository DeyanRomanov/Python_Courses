contest_and_pass = input()

contest_and_pass_dict = {}

while not contest_and_pass == 'end of contests':
    name, password = contest_and_pass.split(':')
    if name not in contest_and_pass_dict:
        contest_and_pass_dict[name] = password
    contest_and_pass = input()


submissions = input()

submissions_dict = {}

while not submissions == 'end of submissions':
    name, passwrd, user, point = submissions.split('=>')
    point = int(point)
    for k, v in contest_and_pass_dict.items():
        if k == name and v == passwrd:
            if user not in submissions_dict and name not in submissions_dict.values():
                submissions_dict[user] = {name: point}
            elif user in submissions_dict and name not in submissions_dict[user]:
                submissions_dict[user][name] = point
            else:
                if submissions_dict[user][name] < point:
                    submissions_dict[user][name] = point
    submissions = input()

max_point = 0
best_user = ''
for k, v in submissions_dict.items():
    total_point = 0
    for score in submissions_dict[k].values():
        total_point += int(score)
    if total_point > max_point:
        best_user = k
        max_point = total_point

print(f"Best candidate is {best_user} with total {max_point} points.\nRanking:")

for k, v in sorted(submissions_dict.items(), key=lambda x: x[0]):
    print(k)
    for keys, values in sorted(submissions_dict[k].items(), reverse=True, key=lambda x: x[1]):
        print(f'#  {keys} -> {values}')
