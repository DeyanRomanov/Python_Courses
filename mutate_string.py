first_word = input()
second_word = input()

last_word = first_word
mutate_word = ''
counter = 0

while True:
    counter += 1
    for x in range(counter):
        mutate_word += second_word[x]
    for y in range(counter, len(second_word)):
        mutate_word += first_word[y]
    if not mutate_word == last_word:
        print(mutate_word)
    last_word = mutate_word
    mutate_word = ''
    if counter == len(first_word):
        break

