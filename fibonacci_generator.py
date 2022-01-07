def fibonacci():
    fb1 = 0
    fb2 = 1
    yield fb1
    yield fb2
    while True:
        fb = fb1 + fb2
        yield fb
        fb1, fb2 = fb2, fb


generator = fibonacci()
for i in range(5):
    print(next(generator))
