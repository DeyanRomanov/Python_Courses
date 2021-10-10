studets = input()

language_counter = {}
students_results = {}

while not studets == 'exam finished':
    studets = studets.split('-')
    if len(studets) > 2:
        name, language, score = studets
        score = int(score)
        if language not in language_counter:
            language_counter[language] = 0
        language_counter[language] += 1
        if name not in students_results:
            students_results[name] = 0
        if students_results[name] <= score:
            students_results[name] = score
    else:
        name = studets[0]
        if name in students_results:
            del students_results[name]
    studets = input()

print('Results:')
for k, v in sorted(students_results.items(), key=lambda x: (-x[1], x[0])):
    print(f'{k} | {v}')
print('Submissions:')
for k, v, in sorted(language_counter.items(), key=lambda x: (-x[1], x[0])):
    print(f'{k} - {v}')