import math


need_time = int(input())
days = int(input())
workers = int(input())
days1 = days * 0.9
hours = (days1 * 8) + (workers * days * 2)
hours = math.floor(hours)
if need_time > hours:
    area = need_time - hours
    print(f'Not enough time!{math.floor(area)} hours needed.')
else:
    area = hours - need_time
    print(f'Yes!{math.floor(area)} hours left.')
