banned_words = input().split(', ')
text_to_change = input()
for word in banned_words:
    while word in text_to_change:
        a = '*' * len(word)
        text_to_change = text_to_change.replace(word, a)
print(text_to_change)