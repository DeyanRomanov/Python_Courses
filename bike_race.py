numbers_of_junior = int(input())
numbers_of_seniors = int(input())
track = input()
area_junior = 0
area_senior = 0
if track == 'trail':
    area_junior = 5.5 * numbers_of_junior
    area_senior = 7 * numbers_of_seniors
elif track == 'cross-country':
    area_junior = 8 * numbers_of_junior
    area_senior = 9.5 * numbers_of_seniors
    if numbers_of_seniors + numbers_of_junior >= 50:
        area_junior *= 0.75
        area_senior *= 0.75
elif track == 'downhill':
    area_junior = 12.25 * numbers_of_junior
    area_senior = 13.75 * numbers_of_seniors
elif track == 'road':
    area_junior = 20 * numbers_of_junior
    area_senior = 21.50 * numbers_of_seniors
total_area = (area_junior + area_senior) * 0.95
print(f'{total_area:.2f}')