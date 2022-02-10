class reverse_iter:
    def __init__(self, item):
        self.item = item
        self.start = 0
        self.end = len(item) - 1
        
    def __iter__(self):
        return self

    def __next__(self):
        if self.end < self.start:
            raise StopIteration
        index = self.end
        self.end -= 1
        return self.item[index]


reversed_list = reverse_iter([1, 2, 3, 4])
for item in reversed_list:
    print(item)

a = 5