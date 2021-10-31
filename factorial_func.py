def factorial(numbers):
    if numbers == 0 or numbers == 1:
        return 1
    return numbers * factorial(numbers - 1)


number = int(input())
print(factorial(number))
