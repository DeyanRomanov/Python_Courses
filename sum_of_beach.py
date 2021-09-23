secret_words = input()

secret_words = secret_words.lower()
words_counter = 0
sun_counter = 0
fish_counter = 0
sand_counter = 0
water_counter = 0
searched_word = ''
while True:
    if 'sand' in secret_words:
        words_counter += 1
        searched_word = 'sand'
        secret_words = secret_words.replace(searched_word, '', 1)
    else:
        sand_counter = 1
    if 'fish' in secret_words:
        words_counter += 1
        searched_word = 'fish'
        secret_words = secret_words.replace(searched_word, '', 1)
    else:
        fish_counter = 1
    if 'water' in secret_words:
        words_counter += 1
        searched_word = 'water'
        secret_words = secret_words.replace(searched_word, '', 1)
    else:
        water_counter = 1
    if 'sun' in secret_words:
        words_counter += 1
        searched_word = 'sun'
        secret_words = secret_words.replace(searched_word, '', 1)
    else:
        sun_counter = 1
    if sun_counter + sand_counter + water_counter + fish_counter == 4:
        break
print(words_counter)

