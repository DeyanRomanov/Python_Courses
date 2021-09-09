record = float(input())
ranges = float(input())
time = float(input())
time_plus = (ranges // 15) * 12.5
total_time = ranges * time + time_plus
if record > total_time:
    print(f'Yes, he succeeded! The new world record is {total_time:.2f} seconds.')
else:
    area = total_time - record
    print(f'No, he failed! He was {area:.2f} seconds slower.')
