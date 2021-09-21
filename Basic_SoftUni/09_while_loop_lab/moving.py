wight_apartment = int(input())
length_apartment = int(input())
height_apartment = int(input())
number_of_box = input()
volume_box = 0
volume_apartment = wight_apartment * length_apartment * height_apartment
while number_of_box != 'Done':
    number_of_box = int(number_of_box)
    volume_box += number_of_box
    if volume_box > volume_apartment:
        print(f'No more free space! You need {abs(volume_apartment - volume_box)} Cubic meters more.')
        break
    else:
        number_of_box = input()
if number_of_box == 'Done':
    print(f'{abs(volume_apartment - volume_box)} Cubic meters left.')
