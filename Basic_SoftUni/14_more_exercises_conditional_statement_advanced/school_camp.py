season = input()
group = input()
numbers_student = int(input())
numbers_nights = int(input())
price = 0
sport = ''
if season == 'Winter':
    if group == 'boys':
        price = numbers_nights * 9.60 * numbers_student
        sport = 'Judo'
    elif group == 'girls':
        price = numbers_nights * 9.60 * numbers_student
        sport = 'Gymnastics'
    elif group == 'mixed':
        price = numbers_nights * 10 * numbers_student
        sport = 'Ski'
elif season == 'Spring':
    if group == 'boys':
        price = numbers_nights * 7.20 * numbers_student
        sport = 'Tennis'
    elif group == 'girls':
        price = numbers_nights * 7.20 * numbers_student
        sport = 'Athletics'
    elif group == 'mixed':
        price = numbers_nights * 9.50 * numbers_student
        sport = 'Cycling'
elif season == 'Summer':
    if group == 'boys':
        price = numbers_nights * 15 * numbers_student
        sport = 'Football'
    elif group == 'girls':
        price = numbers_nights * 15 * numbers_student
        sport = 'Volleyball'
    elif group == 'mixed':
        price = numbers_nights * 20 * numbers_student
        sport = 'Swimming'
if numbers_student >= 50:
    price *= 0.5
elif 50 > numbers_student >= 20:
    price *= 0.85
elif 20 > numbers_student >= 10:
    price *= 0.95
print(f"{sport} {price:.2f} lv.")
