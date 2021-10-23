word = list(input())

reversed_word = ''
while word:
    reversed_word += word.pop()

print(reversed_word)
