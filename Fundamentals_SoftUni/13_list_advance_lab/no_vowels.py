word = input()
exclude_list = ['a', 'o', 'u', 'e', 'i']
word_list = [letter for letter in word if letter.lower() not in exclude_list]
x = ''.join(word_list)
print(x)
