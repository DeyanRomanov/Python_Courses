number = int(input())
counter = 0
while counter <= number:
    counter = (counter * 2) + 1
    if counter > number:
        break
    print(counter)
