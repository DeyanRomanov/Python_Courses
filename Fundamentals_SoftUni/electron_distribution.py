numbers_of_electrons = int(input())
shells_nums = []
total_electrons = 0
is_full = False
while numbers_of_electrons > 0:
    for nums in range(1, 200):
        electrons = 2 * (nums ** 2)
        if electrons <= numbers_of_electrons:
            numbers_of_electrons -= electrons
            shells_nums.append(electrons)
        else:
            if numbers_of_electrons > 0:
                shells_nums.append(numbers_of_electrons)
                is_full = True
                break
    if is_full:
        break
print(shells_nums)
