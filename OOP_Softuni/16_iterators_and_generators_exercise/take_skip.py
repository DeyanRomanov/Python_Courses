class take_skip:
    def __init__(self, step, count):
        self.step = step
        self.count = count
        self.current_num = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count <= 0:
            raise StopIteration
        number = self.current_num
        self.current_num += self.step
        self.count -= 1
        return number


# numbers = take_skip(2, 6)
# for number in numbers:
#     print(number)
#
# numbers = take_skip(10, 5)
# for number in numbers:
#     print(number)
