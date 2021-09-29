code = input().split()
coding_message = input()

' '.join(coding_message)
new_list = []
letter = 0
new_message = ''

for word in code:
    for letters in word:
        letter += int(letters)
    while letter >= len(coding_message):
        letter -= len(coding_message)
    new_message += coding_message[letter]
    coding_message = coding_message[0:letter] + coding_message[letter + 1::]
    letter = 0

print(new_message)

