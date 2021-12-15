class dictionary_iter:
    def __init__(self, dictionary):
        self.dictionary = dictionary
        self.index = 0
        self.keys = list(self.dictionary.keys())
        self.values = list(self.dictionary.values())

    def __iter__(self):
        return self

    def __next__(self):
        if self.index > len(self.dictionary) - 1:
            raise StopIteration
        index = self.index
        current_key = self.keys[index]
        current_value = self.values[index]
        self.index += 1
        return current_key, current_value


result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)
