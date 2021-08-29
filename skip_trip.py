days = int(input())
room = input()
rating = input()
price = 0
days -= 1
if days < 10:
    if room == 'room for one person':
        price = days * 18
    elif room == 'apartment':
        price = days * 25 * 0.7
    elif room == 'president apartment':
        price = days * 35 * 0.9
elif 10 <= days <= 15:
    if room == 'room for one person':
        price = days * 18
    elif room == 'apartment':
        price = days * 25 * 0.65
    elif room == 'president apartment':
        price = days * 35 * 0.85
elif 15 < days:
    if room == 'room for one person':
        price = days * 18
    elif room == 'apartment':
        price = days * 25 * 0.5
    elif room == 'president apartment':
        price = days * 35 * 0.80
if rating == 'positive':
    price = price + (price * 0.25)
elif rating == 'negative':
    price = price - (price * 0.1)
print(f'{price:.2f}')
