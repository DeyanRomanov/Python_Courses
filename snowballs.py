number_of_snowballs = int(input())

snowball_value = 0
last_snowball = 0
snow = 0
time = 0
quality = 0

for snowball in range(number_of_snowballs):
    snowball_value = 0
    snowball_snow = int(input())
    snowball_time = int(input())
    snowball_quality = int(input())
    snowball_value += int((snowball_snow / snowball_time) ** snowball_quality)
    if last_snowball < snowball_value:
        last_snowball = snowball_value
        snow = snowball_snow
        time = snowball_time
        quality = snowball_quality

print(f'{snow} : {time} = {last_snowball} ({quality})')
