day_off = int(input())
work_days = 365 - day_off
work_days_play_minutes = work_days * 63
day_off_play_minutes = day_off * 127
norm_tom_sleep = 30000
total_play_time = work_days_play_minutes + day_off_play_minutes
if total_play_time > norm_tom_sleep:
    print('Tom will run away')
    area = total_play_time - norm_tom_sleep
    hours = area // 60
    minutes = area % 60
    print(f'{hours} hours and {minutes} minutes more for play')
else:
    print('Tom sleeps well')
    area = norm_tom_sleep - total_play_time
    hours = area // 60
    minutes = area % 60
    print(f'{hours} hours and {minutes} minutes less for play')
