import re

words_dict = {}

pattern = r"[A-Za-z]+[']*[A-Za-z]*"

with open('words.txt', 'r') as file, open('input.txt', 'r') as text, open('output.txt', 'w') as output:
    for line in file:
        line = line.split()
        for word in line:
            if word not in words_dict:
                words_dict[word] = 0
    for word in text:
        for match in re.finditer(pattern, word):
            result = match.group().lower()
            if result in words_dict:
                words_dict[result] += 1
    for key, value in sorted(words_dict.items(), key=lambda x: -x[1]):
        output.write(f"{key} - {value}")
        output.write('\n')
