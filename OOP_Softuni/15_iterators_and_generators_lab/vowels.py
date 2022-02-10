class vowels:
    def __init__(self, text):
        self.text = text
        self.start = 0
        self.vowel = [letter for letter in self.text if letter in 'AEIUYOaeiuyo']
        self.end = len(self.vowel) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.start > self.end:
            raise StopIteration
        index = self.start
        self.start += 1
        return self.vowel[index]


# my_string = vowels('Abcedifuty0o')
# for char in my_string:
#     print(char)
