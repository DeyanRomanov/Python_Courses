def is_leap(year):
    leap = False
    if year < 1:
        return leap
    if year % 4 == 0:
        if year % 100 == 0 and not year % 400 == 0:
            leap = False
            return leap
        leap = True

    return leap


year = int(input())
print(is_leap(year))
