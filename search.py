number_of_words = int(input())
needed_word = input()

all_words = []
inculuded_words = []
for words in range(number_of_words):
    word = input()
    all_words.append(word)
    if needed_word in word:
        inculuded_words.append(word)

print(f'{all_words}\n{inculuded_words}')
