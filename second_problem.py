class Multiset:
    def __init__(self):
        self.values = []
        self.result = []

    def add(self, val):
        self.values.append(val)

    def remove(self, val):
        if val in self.values:
            self.values.remove(val)
            return
        return

    def query(self, val):
        return self.__contains__(val)

    def size(self):
        return self.__len__()

    def __contains__(self, val):
        if val in self.values:
            self.result.append(True)
            return True
        self.result.append(False)
        return False

    def __len__(self):
        self.result.append(len(self.values))
        return len(self.values)


test = Multiset()
for x in range(int(input())):
    operations = input().split()
    if len(operations) == 1:
        a = operations[0]
        if a == 'size':
            test.size()
    else:
        operation = operations[0]
        value = int(operations[1])
        if operation == 'add':
            test.add(value)
        elif operation == 'remove':
            test.remove(value)
        elif operation == 'query':
            test.query(value)

print([x for x in test.result])
