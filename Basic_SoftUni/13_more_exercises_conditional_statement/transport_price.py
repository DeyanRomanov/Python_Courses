kilometers = int(input())
time = input()

bus = kilometers * 0.09
train = kilometers * 0.06
taxi_day = kilometers * 0.79 + 0.7
taxi_night = kilometers * 0.9 + 0.7
if kilometers >= 100 and time == 'day':
    if bus > train and taxi_day > train:
        print(f'{train:.2f}')
    elif bus > train and taxi_day < train:
        print(f'{taxi_day:.2f}')
    elif bus < train and taxi_day > bus:
        print(f'{bus:.2f}')
elif kilometers >= 100 and time == 'night':
    if bus > train and taxi_night > train:
        print(f'{train:.2f}')
    elif bus > train and taxi_night < train:
        print(f'{taxi_night:.2f}')
    elif bus < train and taxi_night > bus:
        print(f'{bus:.2f}')
elif 100 > kilometers >= 20 and time == 'day':
    if bus > taxi_day:
        print(f'{taxi_day:.2f}')
    elif taxi_day > bus:
        print(f'{bus:.2f}')
elif 100 > kilometers >= 20 and time == 'night':
    if bus > taxi_night:
        print(f'{taxi_night:.2f}')
    elif taxi_night > bus:
        print(f'{bus:.2f}')
elif kilometers < 20 and time == 'night':
    print(f'{taxi_night:.2f}')
elif kilometers < 20 and time == 'day':
    print(f'{taxi_day:.2f}')
