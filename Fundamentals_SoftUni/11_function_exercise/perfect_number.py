def perfect_number(num):
    perfect = 0
    for x in range(1, num + 1):
        if num % x == 0 and x < num:
            perfect += x
    if perfect == num:
        return 'We have a perfect number!'
    else:
        return "It's not so perfect."


number = int(input())

print(perfect_number(number))
