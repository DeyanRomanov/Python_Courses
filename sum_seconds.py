first = int(input())
second = int(input())
third = int(input())
time_seconds = first + second + third
time_minutes = time_seconds // 60
time_seconds %= 60
print(f'{time_minutes}:{time_seconds:02d}')
