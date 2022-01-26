# Given a time in
# -hour AM/PM format, convert it to military (24-hour) time.
# Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
# - 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.
# Return '12:01:00'.
# Return '00:01:00'.
clock = input()
what_is_time = clock[-2::]
hour = clock[:2]
if what_is_time == "PM":
    hour = int(clock[:2]) + 12
    if hour == 24:
        hour = 12
else:
    if hour == '12':
        hour = '00'
clock = f'{hour}{clock[2:-2]}'
print(clock)

